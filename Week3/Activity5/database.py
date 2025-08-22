import sqlite3

def create_connection():
    conn = sqlite3.connect("user.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF  NOT EXISTS users(
            id INTEGER  PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
            )
        ''')
    
    cursor.execute('''
        CREATE TABLE IF  NOT EXISTS students(
            std_id INTEGER  PRIMARY KEY AUTOINCREMENT,
            std_name TEXT NOT NULL,
            std_address TEXT NOT NULL
            )
        ''')
    conn.commit()
    conn.close()
    