import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            std_id INTEGER PRIMARY KEY AUTOINCREMENT,
            std_name TEXT NOT NULL,
            std_address TEXT NOT NULL,
            std_email TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturer (
            Lct_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Lct_name TEXT NOT NULL,
            Lct_email TEXT NOT NULL UNIQUE,
            Lct_depatment TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS class (
            class_room_no INTEGER
        )
    ''')
    conn.commit()
    conn.close()
