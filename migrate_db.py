import sqlite3
import os

DB_NAME = 'iskcon.db'

def migrate():
    if not os.path.exists(DB_NAME):
        print("Database not found, nothing to migrate.")
        return

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    try:
        print("Attempting to add 'purpose' column...")
        c.execute('ALTER TABLE donations ADD COLUMN purpose TEXT')
        conn.commit()
        print("Success: 'purpose' column added.")
    except sqlite3.OperationalError as e:
        if 'duplicate column' in str(e):
            print("Column 'purpose' already exists.")
        else:
            print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
