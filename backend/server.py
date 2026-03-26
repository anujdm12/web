from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

# Import database functions (same folder as server.py)
from database import init_database, add_contact, get_visitor_count, increment_visitor_count, get_all_contacts, delete_contact

# ==================== PATH SETUP ====================

# Get absolute path to project root (one level up from backend)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PORTFOLIO_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

# ==================== APP SETUP ====================

app = Flask(__name__, static_folder=PORTFOLIO_DIR)
CORS(app)

# Initialize database
init_database()

# ==================== STATIC ROUTES ====================

@app.route('/')
def index():
    return send_from_directory(PORTFOLIO_DIR, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(PORTFOLIO_DIR, path)

# ==================== ADMIN ====================

@app.route('/admin')
def admin():
    return send_from_directory(PORTFOLIO_DIR, 'admin.html')

# ==================== API ROUTES ====================

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()

        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not message:
            return jsonify({'error': 'All fields are required'}), 400

        if '@' not in email or '.' not in email:
            return jsonify({'error': 'Invalid email address'}), 400

        success = add_contact(name, email, message)

        if success:
            return jsonify({
                'message': 'Thank you for your message!',
                'success': True
            }), 200
        else:
            return jsonify({'error': 'Failed to save message'}), 500

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/stats', methods=['GET'])
def stats():
    try:
        visitor_count = get_visitor_count()

        return jsonify({
            'visitors': visitor_count,
            'success': True
        }), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'Server is running'
    }), 200


@app.route('/api/visit', methods=['POST'])
def visit():
    try:
        visitor_count = increment_visitor_count()
        return jsonify({
            'visitors': visitor_count,
            'success': True
        }), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/messages', methods=['GET'])
def messages():
    try:
        contacts = get_all_contacts()
        items = []
        for contact in contacts:
            items.append({
                'id': contact['id'],
                'name': contact['name'],
                'email': contact['email'],
                'message': contact['message'],
                'created_at': contact['created_at']
            })

        return jsonify({
            'success': True,
            'total': len(items),
            'messages': items
        }), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Internal server error', 'success': False}), 500


@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def remove_message(message_id):
    try:
        deleted = delete_contact(message_id)
        if not deleted:
            return jsonify({'success': False, 'error': 'Message not found'}), 404
        return jsonify({'success': True}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Internal server error', 'success': False}), 500


# ==================== RUN SERVER ====================

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
