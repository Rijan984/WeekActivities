from database import create_connection
import sqlite3

def add_student(name, email, address):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (std_name, std_address, std_email) VALUES (?, ?, ?)", (name, address, email))
        conn.commit()
        print("Student added successfully")
    except sqlite3.IntegrityError:
        print("Email must be unique")
    conn.close()

def add_lecturer(name, email, department):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lecturer (Lct_name, Lct_email, LCT_department) VALUES (?, ?, ?)", (name, email, department))
        conn.commit()
        print("Lecturer added successfully")
    except sqlite3.IntegrityError:
        print("Enter unique email")
    conn.close()

def add_class(class_no):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO class (class_room_no) VALUES (?)", (class_no))
    conn.commit()
    conn.close()

def view_student():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_students(std_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE std_id = ?", (std_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")