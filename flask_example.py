from flask import Flask, request, jsonify, url_for
from collections import OrderedDict
import sqlite3

app = Flask(__name__)

# データベース接続
def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn

# データベース初期化
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            stock_amount INTEGER NOT NULL
         )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        amount_sold INTEGER NOT NULL,
        total_price REAL NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# 初期化は一回のみ
init_db()

# ルーティングとは、URLとFlaskの処理を対応づけることで、URLと関数を紐付けることが出来ます。
# Flaskでルーティングを記述するには、route()を用います。
# (1)在庫作成
@app.route('/v1/stocks', methods=['POST'])
def create_product():

    if not request.is_json:  # リクエストがJSON形式か確認
        return jsonify({"message": "Invalid Content-Type"}), 400

    data = request.get_json()

    product_name = data.get('name')
    stock_amount = data.get('amount', 1)

    print(f"Product name is {product_name}, with amount of {stock_amount}.")

    print("Here!")
    if not product_name or not isinstance(stock_amount, int):
        print("Oops Here!")
        return jsonify({"message": "ERROR"}), 400
    
    conn = get_db_connection()
    conn.execute('INSERT INTO products (product_name, stock_amount) VALUES (?,?)', (product_name, stock_amount))
    conn.commit()
    conn.close()

    return jsonify({"name": product_name, "amount": stock_amount}), 201

# @app.routeの関数内の<・・・>の部分に任意の名前(ここでは)を記述することで、
# その名称を次の関数(ここではhello関数)にてroute内の<・・・>で記述した値を引数として利用することが可能になります。
# 今回は’/hello/’としましたが、<・・・>の・・・の部分は自由な名称をつけることが可能です。

# (2)在庫問合せ
@app.route('/v1/stocks', methods=['GET'])
@app.route('/v1/stocks/<name>', methods=['GET'])
def get_stocks(name=None):
    conn = get_db_connection()

    # http://127.0.0.1:5000/v1/stocks/<name>: 指名されたアイテムのみ
    if name:
        product = conn.execute('SELECT * FROM products WHERE product_name = ?', (name,)).fetchone()
        conn.close()

        if product:
            return jsonify({name: product['stock_amount']})
        else:
            return jsonify({name: 0})

    # http://127.0.0.1:5000/v1/stocks: 全ての在庫を出力
    else:
        products = conn.execute('SELECT * FROM products WHERE stock_amount > 0 ORDER BY product_name ASC').fetchall()
        conn.close()

        result = {product['product_name']: product['stock_amount'] for product in products}
        return jsonify(result)

# (3)販売
@app.route('/v1/sales', methods=['POST'])
def sale_execute():
    data = request.json
    product_name = data.get('name')
    amount = data.get('amount', 1)
    price = data.get('price')

    # リクエスト検証： nameは必須、amountとpriceは任意
    if not product_name or not isinstance(amount, int) or amount <= 0:
        return jsonify({"message": "ERROR"}), 400
    
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE product_name = ?', (product_name,)).fetchone()
    
    # 商品が存在しない
    if not product:
        conn.close()
        return jsonify({"message": f"Product '{product_name}' not found"}), 404
    
    # 在庫が足りない
    if product['stock_amount'] < amount:
        conn.close()
        return jsonify({"message": "Not enough stock"}), 400
    
    # 在庫を更新する
    new_stock_amount = product['stock_amount'] - amount
    conn.execute('UPDATE products SET stock_amount = ? WHERE product_name = ?', (new_stock_amount, product_name))

    response = jsonify({"name": product_name, "amount": amount})

    # 売り上げを計算する（price自体が存在かつ0より大きい）
    total_price = 0
    if price and isinstance(price, (int, float)) and price > 0:
        total_price = price * amount
        conn.execute('INSERT INTO sales (product_name, amount_sold, total_price) VALUES (?, ?, ?)', 
        (product_name, amount, total_price))
        # priceがあればレスポンスに入れる
        response = jsonify(OrderedDict([("name", product_name), ("amount", amount), ("price", price)]))
        # response = jsonify({"name": product_name, "amount": amount, "price": price})

    conn.commit()
    conn.close()

    response.headers['Location'] = url_for('get_sales', name=product_name, _external=True)

    return response, 200

# 売り上げ確認
@app.route('/v1/sales', methods=['GET'])
def get_sales_sum():
    conn = get_db_connection()
    result = conn.execute('SELECT SUM(total_price) FROM sales').fetchone()
    conn.close()

    sales_sum = result[0] if result[0] is not None else 0 
    return jsonify({"sales": sales_sum})

@app.route('/v1/sales/amount', methods=['GET'])
def get_amount_sum():
    conn = get_db_connection()
    result = conn.execute('SELECT SUM(amount_sold) FROM sales').fetchone()
    conn.close()

    amount_sum = result[0] if result[0] is not None else 0
    return jsonify({"amount": amount_sum})

@app.route('/v1/sales/<name>', methods=['GET'])
def get_sales(name):
    conn = get_db_connection()
    sales = conn.execute('SELECT * FROM sales WHERE product_name = ?', (name)).fetchall()
    conn.close()

    if not sales:
        return jsonify({"message": f"No sales records for '{name}'"}), 404

    total_sales = []
    for sale in sales:
        total_sales.append({"amount_sold": sale['amount_sold'], "total_price": sale["total_price"]})

    return jsonify(total_sales)

# @app.route('/v1/products/<int:id>', methods=['PUT'])
# def update_product(id):
#     data = request.json
#     stock_amount = data.get('stock_amount')

#     if not isinstance(stock_amount, int):
#         return jsonify({"message": "ERROR"}), 400
    
#     conn = get_db_connection()
#     conn.execute('UPDATE prodcts SET stock_amount = ? WHERE id = ?', (stock_amount, id))
#     conn.commit()
#     conn.close()

#     return jsonify({"id": id, "new_stock_amount": stock_amount})

# 個別で商品を削除
@app.route('/v1/stocks/<int:id>', methods=['DELETE'])
def delete_item(id):
    conn = get_db_connection
    conn.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Product deleted", "id": id})

# 全削除
@app.route('/v1/stocks', methods=['DELETE'])
def delete_all_stocks():
    conn = get_db_connection()

    # productテーブル
    conn.execute('DELETE FROM products')

    # salesテーブル
    conn.execute('DELETE FROM sales')

    conn.commit()
    conn.close()

    return jsonify({"message": "All stocks and sales data have been successfully deleted."}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)