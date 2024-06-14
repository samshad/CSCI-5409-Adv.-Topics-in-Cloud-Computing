import os
from mysql.connector import connect, Error
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}


def create_connection():
    """
    Create a database connection to the MySQL database specified in db_config.

    Returns:
        connection (mysql.connector.connection.MySQLConnection): MySQL database connection object.
    """
    try:
        connection = connect(**db_config)
        if connection.is_connected():
            print("Successfully connected to the database!")
            return connection
    except Error as e:
        print(f"Error: {e}!")
        return None


def create_table():
    """
    Create the products table in the database if it does not already exist.
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        name VARCHAR(100),
        price VARCHAR(100),
        availability BOOLEAN
    );
    """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(create_table_query)
            connection.commit()
            print("Table 'products' created successfully!")
        except Error as e:
            print(f"Error: {e}!")
        finally:
            cursor.close()
            connection.close()


def insert_product(name, price, availability):
    """
    Insert a product into the products table.

    Parameters:
        name (str): The name of the product.
        price (str): The price of the product.
        availability (bool): The availability status of the product.
   """
    # Ensure the products table exists
    create_table()

    insert_query = "INSERT INTO products (name, price, availability) VALUES (%s, %s, %s)"
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(insert_query, (name, price, availability))
            connection.commit()
            print("Product inserted successfully!")
        except Error as e:
            print(f"Error: {e}!")
        finally:
            cursor.close()
            connection.close()


def get_all_products():
    """
    Retrieve all products from the products table.

    Returns:
        products (list): A list of dictionaries representing the products.
    """
    select_query = "SELECT name, price, availability FROM products"
    connection = create_connection()
    products = []
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(select_query)
            result = cursor.fetchall()
            for row in result:
                products.append({
                    'name': row[0],
                    'price': row[1],
                    'availability': bool(row[2])
                })
            print("Products retrieved successfully!")
            return products
        except Error as e:
            print(f"Error: {e}!")
            return []
        finally:
            cursor.close()
            connection.close()


def drop_table():
    """
    Drop the products table from the database.
    """
    drop_table_query = "DROP TABLE IF EXISTS products;"
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(drop_table_query)
            connection.commit()
            print("Table 'products' dropped successfully!")
        except Error as e:
            print(f"Error: {e}!")
        finally:
            cursor.close()
            connection.close()
