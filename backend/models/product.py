from models.database import get_db_connection

def get_all_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, stock, brand FROM products")
    products = cursor.fetchall()
    cursor.close()
    return products
