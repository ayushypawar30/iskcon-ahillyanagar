import sqlite3
import os

DB_NAME = 'iskcon.db'

def check_order(order_id):
    if not os.path.exists(DB_NAME):
        print("Database file not found!")
        return

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    print(f"--- Checking for Order ID: {order_id} ---")
    c.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
    row = c.fetchone()
    
    if row:
        print("FOUND:")
        print(dict(row))
    else:
        print("NOT FOUND")
        
    print("\n--- All Orders ---")
    c.execute("SELECT order_id, customer_name, date FROM orders")
    rows = c.fetchall()
    for r in rows:
        print(dict(r))

    conn.close()

if __name__ == "__main__":
    check_order('ORD-1764684942089')
