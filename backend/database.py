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

    # Orders Table (New)
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT,
            customer_name TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            city TEXT,
            zip TEXT,
            items TEXT,
            total_amount REAL,
            payment_mode TEXT,
            status TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Users Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            phone TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Volunteers Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            service TEXT,
            festival TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Attempt to add festival column if it doesn't exist (migration)
    try:
        c.execute('ALTER TABLE volunteers ADD COLUMN festival TEXT')
    except sqlite3.OperationalError:
        pass # Column likely already exists

    # Bookings Table (Pooja/Seva)
    c.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            date TEXT,
            status TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Marathon Orders Table (New)
    c.execute('''
        CREATE TABLE IF NOT EXISTS marathon_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            email TEXT,
            books_summary TEXT,  -- e.g., "Gita (2), Bhagavatam (1)"
            total_qty INTEGER,
            status TEXT,         -- "Pending", "Collected"
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # RSVPs Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS rsvps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT,
            name TEXT,
            phone TEXT,
            guests INTEGER,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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

def save_order(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO orders (order_id, customer_name, email, phone, address, city, zip, items, total_amount, payment_mode, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('orderId'),
        data.get('name'),
        data.get('email'),
        data.get('phone'),
        data.get('address'),
        data.get('city'),
        data.get('zip'),
        data.get('items'),
        data.get('total'),
        data.get('paymentMode'),
        data.get('status', 'Pending')
    ))
    conn.commit()
    last_id = c.lastrowid
    conn.close()
    return {'status': 'success', 'id': last_id}

def get_orders():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM orders ORDER BY date DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_order_by_id(order_id):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM orders WHERE order_id = ?', (order_id,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None

def update_order_status(order_id, status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('UPDATE orders SET status = ? WHERE order_id = ?', (status, order_id))
    conn.commit()
    updated = c.rowcount > 0
    conn.close()
    return updated

def create_user(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (name, email, password, phone) VALUES (?, ?, ?, ?)', 
                 (data.get('name'), data.get('email'), data.get('password'), data.get('phone')))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(email, password):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
    user = c.fetchone()
    conn.close()
    return dict(user) if user else None

def get_users():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM users ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_orders_by_email(email):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM orders WHERE email = ? ORDER BY date DESC', (email,))
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# --- New Functions ---

def save_volunteer(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO volunteers (name, phone, service, festival) VALUES (?, ?, ?, ?)',
              (data.get('name'), data.get('phone'), data.get('service'), data.get('festival')))
    conn.commit()
    conn.close()

def get_volunteers():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM volunteers ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def save_booking(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO bookings (name, type, date, status) VALUES (?, ?, ?, ?)',
              (data.get('name'), data.get('type'), data.get('date'), 'Confirmed'))
    conn.commit()
    conn.close()

def get_bookings():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM bookings ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def save_rsvp(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO rsvps (event_name, name, phone, guests) VALUES (?, ?, ?, ?)',
              (data.get('eventName'), data.get('name'), data.get('phone'), data.get('guests')))
    conn.commit()
    conn.close()

def save_marathon_order(data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO marathon_orders (name, phone, email, books_summary, total_qty, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data.get('name'), 
        data.get('phone'), 
        data.get('email'), 
        data.get('books_summary'), 
        data.get('total_qty'), 
        'Pending'
    ))
    conn.commit()
    conn.close()

def get_marathon_orders():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM marathon_orders ORDER BY date DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_rsvps():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM rsvps ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def clear_table(table_name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Whitelist tables for safety
    if table_name in ['donations', 'contacts', 'subscribers', 'orders', 'users', 'volunteers', 'bookings', 'rsvps']:
        c.execute(f'DELETE FROM {table_name}')
        conn.commit()
    conn.close()
