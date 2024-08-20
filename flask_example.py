from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# データベース接続
def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            stock_amount INTEGER NOT NULL
         )
''')
    conn.commit()
    conn.close()

init_db()

@app.route('/v1/products', methods=['POST'])
def create_product():

    if not request.is_json:  # リクエストがJSON形式か確認
        return jsonify({"message": "Invalid Content-Type"}), 400

    data = request.get_json()
    product_name = data.get('product_name')
    stock_amount = data.get('stock_amount', 1)
    print("Here!")
    if not product_name or not isinstance(stock_amount, int):
        print("Oops Here!")
        return jsonify({"message": "ERROR"}), 400
    
    conn = get_db_connection()
    conn.execute('INSERT INTO products (product_name, stock_amount) VALUES (?,?)', (product_name, stock_amount))
    conn.commit()
    conn.close()

    return jsonify({"product_name": product_name, "stock_amount": stock_amount}), 201

@app.route('/v1/stocks', methods=['GET'])
@app.route('/v1/stocks/<name>', methods=['GET'])
def get_stocks(name=None):
    conn = get_db_connection()

    if name:
        product = conn.execute('SELECT * FROM products WHERE product_name = ?', (name,)).fetchone()
        conn.close()

        if product:
            return jsonify({name: product['stock_amount']})
        else:
            return jsonify({name: 0})

    else:
        products = conn.execute('SELECT * FROM products WHERE stock_amount > 0 ORDER BY product_name ASC').fetchall()
        conn.close()

        result = {product['product_name']: product['stock_amount'] for product in products}
        return jsonify(result)

@app.route('/v1/sales', methods=['POST'])
def sale_execute():
    data = request.json
    product_name = data.get('name')
    amount = data.get('amount', 1)
    price = data.get('price')

    if not product_name or not isinstance(amount, int) or amount <= 0:
        return jsonify({"message": "ERROR"}), 400
    
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE product_name = ?', (product_name,)).fetchone()
    
    if not product:
        conn.close()
        return jsonify({"message": f"Product '{product_name}' not found"}), 404
    
    if product['stock_amount'] < amount:
        conn.close()
        return jsonify({"message": "Not enough stock"}), 400
    
    new_stock_amount = product['stock_amount'] - amount
    conn.execute('UPDATE products SET stock_amount = ? WHERE product_name = ?', (new_stock_amount, product_name))

    total_price = 0
    if price and isinstance(price, (int, float)) and price > 0:
        total_price = price * amount
        conn.execute('INSERT INTO sales (product_name, amount_sold, total_price) VALUES (?, ?, ?)', (product_name, amount, total_price))

    conn.commit()
    conn.close()

    response = jsonify({"name": product_name, "amount": amount})
    response.headers['Location'] = url_for('get_sales', name=product_name, _external=True)

    return response, 200

@app.route('/v1/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    stock_amount = data.get('stock_amount')

    if not isinstance(stock_amount, int):
        return jsonify({"message": "ERROR"}), 400
    
    conn = get_db_connection()
    conn.execute('UPDATE prodcts SET stock_amount = ? WHERE id = ?', (stock_amount, id))
    conn.commit()
    conn.close()

    return jsonify({"id": id, "new_stock_amount": stock_amount})

@app.route('/v1/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    conn = get_db_connection
    conn.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Product deleted", "id": id})

if __name__ == '__main__':
    app.run(port=5000)

