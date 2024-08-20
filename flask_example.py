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

@app.route('/v1/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products'). fetchall
    conn.close()

    products_list = []
    for product in products:
        products_list.append({"id": product["id"], "product_name": product["product_name"], "stock_amount": product["stock_amount"]})

    return jsonify(products_list)


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

