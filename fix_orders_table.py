import sqlite3
import os

DB_NAME = 'iskcon.db'

def fix_table():
    if not os.path.exists(DB_NAME):
        return

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    print("Dropping old orders table...")
    c.execute("DROP TABLE IF EXISTS orders")
    conn.commit()
    print("Table dropped. Restart the server to recreate it.")
    
    conn.close()

if __name__ == "__main__":
    fix_table()
