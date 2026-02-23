import sqlite3

def check_db():
    try:
        conn = sqlite3.connect('iskcon.db')
        c = conn.cursor()
        
        # Check schema
        print("--- Table Schema ---")
        for row in c.execute("PRAGMA table_info(donations)"):
            print(row)
            
        # Check data
        print("\n--- Recent Donations ---")
        for row in c.execute("SELECT * FROM donations ORDER BY id DESC LIMIT 5"):
            print(row)
            
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_db()
