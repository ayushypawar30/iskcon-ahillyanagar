import sqlite3
import os

DB_NAME = 'iskcon.db'

def inspect_donations():
    if not os.path.exists(DB_NAME):
        print("Database not found!")
        return

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    print("--- RAW DONATION DATA ---")
    c.execute('SELECT id, donor_name, amount, purpose FROM donations')
    rows = c.fetchall()
    
    if not rows:
        print("No donations found.")
    
    for row in rows:
        print(f"ID: {row['id']}, Name: {row['donor_name']}, Amount: {row['amount']}, Purpose: '{row['purpose']}'")

    conn.close()

if __name__ == "__main__":
    inspect_donations()
