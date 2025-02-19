import sqlite3

# Function to create the database and table
def create_db():
    conn = sqlite3.connect('contact_messages.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Function to save the contact form data into the database
def save_message(name, email, message):
    conn = sqlite3.connect('contact_messages.db')
    cursor = conn.cursor()

    # Insert the form data into the 'messages' table
    cursor.execute('''
        INSERT INTO messages (name, email, message)
        VALUES (?, ?, ?)
    ''', (name, email, message))

    conn.commit()
    conn.close()
