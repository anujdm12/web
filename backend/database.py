import sqlite3
import os
from datetime import datetime

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), 'portfolio.db')

def get_connection():
    """Create a database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initialize the database with required tables"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create contacts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create visitor stats table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitor_stats (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            count INTEGER DEFAULT 0,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Initialize visitor count if not exists
    cursor.execute('INSERT OR IGNORE INTO visitor_stats (id, count) VALUES (1, 0)')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

def add_contact(name, email, message):
    """Add a new contact message"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO contacts (name, email, message)
            VALUES (?, ?, ?)
        ''', (name, email, message))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error adding contact: {e}")
        return False

def get_all_contacts():
    """Get all contact messages"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM contacts ORDER BY created_at DESC')
        contacts = cursor.fetchall()
        
        conn.close()
        return contacts
    except Exception as e:
        print(f"Error getting contacts: {e}")
        return []

def get_visitor_count():
    """Get current visitor count"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT count FROM visitor_stats WHERE id = 1')
        result = cursor.fetchone()
        
        conn.close()
        return result['count'] if result else 0
    except Exception as e:
        print(f"Error getting visitor count: {e}")
        return 0

def increment_visitor_count():
    """Increment and return visitor count"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE visitor_stats 
            SET count = count + 1, last_updated = CURRENT_TIMESTAMP 
            WHERE id = 1
        ''')
        
        cursor.execute('SELECT count FROM visitor_stats WHERE id = 1')
        result = cursor.fetchone()
        
        conn.commit()
        conn.close()
        
        return result['count'] if result else 0
    except Exception as e:
        print(f"Error incrementing visitor count: {e}")
        return 0

if __name__ == '__main__':
    # Initialize database when run directly
    init_database()
    print("Database setup complete!")
