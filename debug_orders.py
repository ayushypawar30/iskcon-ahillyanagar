import sqlite3
import os

DB_NAME = 'iskcon.db'

def check_db():
    if not os.path.exists(DB_NAME):
        print("Database file not found!")
        return

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # Check tables
    print("--- Tables ---")
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    for t in tables:
        print(t[0])
        
    # Check orders columns
    print("\n--- Orders Table Info ---")
    try:
        c.execute("PRAGMA table_info(orders)")
        columns = c.fetchall()
        for col in columns:
            print(col)
            
        # Try inserting
        print("\n--- Attempting Insert ---")
        c.execute('''
            INSERT INTO orders (order_id, customer_name, email, phone, address, city, zip, items, total_amount, payment_mode, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', ('TEST-001', 'Test User', 'test@example.com', '1234567890', '123 St', 'City', '00000', '[]', 100.0, 'cod', 'Pending'))
        conn.commit()
        print("Insert successful!")
        
        # Clean up
        c.execute("DELETE FROM orders WHERE order_id='TEST-001'")
        conn.commit()
        
    except Exception as e:
        print(f"Error: {e}")

    conn.close()

if __name__ == "__main__":
    check_db()
