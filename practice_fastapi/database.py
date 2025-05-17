import sqlite3

DB_FILE = "users.db"

def connect_db():
    # Connect to the database file (create if it does not exist)
    conn = sqlite3.connect(DB_FILE)
   #refrenced from https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    # Create users table if it doesn't exist yet
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT
        )
    """)
    connection.commit()
    connection.close()
