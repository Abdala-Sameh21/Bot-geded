import sqlite3

def create_tables():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                      (id INTEGER PRIMARY KEY, status TEXT)''')
    conn.commit()
    conn.close()

def update_order_status(order_id, status):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
    conn.commit()
    conn.close()
