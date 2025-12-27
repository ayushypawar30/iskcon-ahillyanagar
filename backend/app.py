from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import database

app = Flask(__name__, static_folder='../')
CORS(app)

# Initialize DB on start
database.init_db()

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# --- API Endpoints ---

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    if database.create_user(data):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'error': 'Email already exists'}), 400

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = database.verify_user(data.get('email'), data.get('password'))
    if user:
        return jsonify({'status': 'success', 'user': user})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/users', methods=['GET', 'DELETE'])
def handle_users():
    if request.method == 'GET':
        return jsonify(database.get_users())
    elif request.method == 'DELETE':
        database.clear_table('users')
        return jsonify({'status': 'success', 'message': 'Users cleared'})

@app.route('/api/book-marathon', methods=['POST'])
def book_marathon():
    data = request.json
    database.save_marathon_order(data)
    return jsonify({'status': 'success', 'message': 'Booking confirmed'})

@app.route('/api/book-bookings', methods=['GET']) # Renamed to match admin.html expectation if needed, or update admin.html
def get_marathon_bookings():
    # Admin.html calls /api/book-bookings for the "Book Marathon" tab
    return jsonify(database.get_marathon_orders())

@app.route('/api/my-orders', methods=['GET'])
def my_orders():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'Email required'}), 400
    orders = database.get_orders_by_email(email)
    return jsonify(orders)

@app.route('/api/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = database.get_order_by_id(order_id)
    if order:
        return jsonify(order)
    else:
        return jsonify({'error': 'Order not found'}), 404

@app.route('/api/orders/<order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    data = request.json
    status = data.get('status')
    if database.update_order_status(order_id, status):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'error': 'Failed to update'}), 400

@app.route('/api/orders', methods=['GET', 'POST'])
def handle_orders():
    if request.method == 'POST':
        data = request.json
        result = database.save_order(data)
        return jsonify(result)
    else:
        orders = database.get_orders()
        return jsonify(orders)

@app.route('/api/donations', methods=['GET', 'POST', 'DELETE'])
def handle_donations():
    if request.method == 'POST':
        data = request.json
        database.save_donation(data)
        return jsonify({'status': 'success', 'message': 'Donation saved'})
    elif request.method == 'GET':
        return jsonify(database.get_donations())
    elif request.method == 'DELETE':
        database.clear_table('donations')
        return jsonify({'status': 'success', 'message': 'Donations cleared'})

@app.route('/api/contacts', methods=['GET', 'POST', 'DELETE'])
def handle_contacts():
    if request.method == 'POST':
        data = request.json
        database.save_contact(data)
        return jsonify({'status': 'success', 'message': 'Contact saved'})
    elif request.method == 'GET':
        return jsonify(database.get_contacts())
    elif request.method == 'DELETE':
        database.clear_table('contacts')
        return jsonify({'status': 'success', 'message': 'Contacts cleared'})

@app.route('/api/subscribers', methods=['GET', 'POST', 'DELETE'])
def handle_subscribers():
    if request.method == 'POST':
        email = request.json.get('email')
        success = database.save_subscriber(email)
        if success:
            return jsonify({'status': 'success', 'message': 'Subscriber added'})
        else:
            return jsonify({'status': 'error', 'message': 'Email already exists'}), 400
    elif request.method == 'GET':
        return jsonify(database.get_subscribers())
    elif request.method == 'DELETE':
        database.clear_table('subscribers')
        return jsonify({'status': 'success', 'message': 'Subscribers cleared'})

@app.route('/api/volunteers', methods=['GET', 'POST', 'DELETE'])
def handle_volunteers():
    if request.method == 'POST':
        data = request.json
        database.save_volunteer(data)
        return jsonify({'status': 'success', 'message': 'Volunteer registered'})
    elif request.method == 'GET':
        return jsonify(database.get_volunteers())
    elif request.method == 'DELETE':
        database.clear_table('volunteers')
        return jsonify({'status': 'success', 'message': 'Volunteers cleared'})

@app.route('/api/bookings', methods=['GET', 'POST', 'DELETE'])
def handle_bookings():
    if request.method == 'POST':
        data = request.json
        database.save_booking(data)
        return jsonify({'status': 'success', 'message': 'Booking confirmed'})
    elif request.method == 'GET':
        return jsonify(database.get_bookings())
    elif request.method == 'DELETE':
        database.clear_table('bookings')
        return jsonify({'status': 'success', 'message': 'Bookings cleared'})

@app.route('/api/rsvps', methods=['GET', 'POST', 'DELETE'])
def handle_rsvps():
    if request.method == 'POST':
        data = request.json
        database.save_rsvp(data)
        return jsonify({'status': 'success', 'message': 'RSVP confirmed'})
    elif request.method == 'GET':
        return jsonify(database.get_rsvps())
    elif request.method == 'DELETE':
        database.clear_table('rsvps')
        return jsonify({'status': 'success', 'message': 'RSVPs cleared'})

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("Starting ISKCON Server...")
    print(f"Local Access: http://localhost:{port}")
    app.run(debug=True, host='0.0.0.0', port=port)
