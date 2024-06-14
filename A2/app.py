from flask import Flask, request, jsonify
from db import create_table, insert_product, get_all_products, drop_table

app = Flask(__name__)

# Ensure the products table exists
create_table()


@app.route('/store-products', methods=['POST'])
def store_products():
    """
    Endpoint to store products in the database.
    Expects a JSON body with a list of products.
    """
    try:
        data = request.json
        products = data.get('products', [])
        for product in products:
            name = product.get('name')
            price = product.get('price')
            availability = product.get('availability')
            insert_product(name, price, availability)
        return jsonify({"message": "Success."}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 400


@app.route('/list-products', methods=['GET'])
def list_products():
    """
    Endpoint to list all products in the database.
    Returns a JSON response with a list of products.
    """
    try:
        products = get_all_products()

        if products:
            return jsonify({"products": products}), 200
        else:
            return jsonify({"products": []}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500


@app.route('/drop-table', methods=['GET'])
def drop_products_table():
    try:
        drop_table()
        return jsonify({"message": "Table 'products' dropped successfully."}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500


@app.route('/health', methods=['GET'])
def check_health():
    """
    Endpoint to check the health status of the application.
    """
    try:
        return jsonify({"Health Status": "Live!"}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
