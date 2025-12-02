import sqlite3
import os
from datetime import datetime

DB_NAME = 'iskcon.db'

def init_db():
    """Initialize the database with tables."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # Donations Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS donations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            donor_name TEXT,
            amount REAL,
            email TEXT,
            order_id TEXT,
            purpose TEXT,
            status TEXT,
            date TEXT
        )
    ''')
    
    # Contacts Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT,
            date TEXT
        )
    ''')
    
    # Subscribers Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            date TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized.")

def save_donation(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO donations (donor_name, amount, email, order_id, purpose, status, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (data.get('donorName'), data.get('amount'), data.get('email'), data.get('orderId'), data.get('purpose', 'General'), 'Completed', datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_donations():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM donations ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def save_contact(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO contacts (name, email, message, date)
        VALUES (?, ?, ?, ?)
    ''', (data.get('name'), data.get('email'), data.get('message'), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_contacts():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM contacts ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def save_subscriber(email):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO subscribers (email, date) VALUES (?, ?)', (email, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_subscribers():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM subscribers ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def clear_table(table_name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Whitelist tables for safety
    if table_name in ['donations', 'contacts', 'subscribers']:
        c.execute(f'DELETE FROM {table_name}')
        conn.commit()
    conn.close()
