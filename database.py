import sqlite3
from contextlib import contextmanager

sqlite_file_name = "school.db"

@contextmanager
def get_db_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()

def create_table():
    with get_db_connection() as connection:
        # 1. Students Table
        connection.execute('''CREATE TABLE IF NOT EXISTS students(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        email TEXT NOT NULL,
                        country TEXT NOT NULL,
                        id_number INTEGER NOT NULL
                        )''')
        
        # 2. Teachers Table (5 attributes)
        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        department TEXT NOT NULL,
                        office_room TEXT NOT NULL,
                        employee_id INTEGER NOT NULL
                        )''')
        
        # 3. Courses Table (5 attributes)
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        course_code TEXT NOT NULL,
                        title TEXT NOT NULL,
                        credits INTEGER NOT NULL,
                        semester TEXT NOT NULL,
                        teacher_id INTEGER NOT NULL
                        )''')

# ==========================================
# STUDENT FUNCTIONS (Your original code)
# ==========================================

def add_student(name, age, email, country, id_number):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO students (name, age, email, country, id_number) VALUES (?,?,?,?,?)',
            (name, age, email, country, id_number),
        )
    
def get_student():
    with get_db_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall()

def update_student(id_number, name, age, email, country):
    with get_db_connection() as connection:
        connection.execute(
            '''UPDATE students
                SET name = ?, age = ?, email = ?, country = ?
                WHERE id_number = ?''',
            (name, age, email, country, id_number)
        )

def delete_student(id_number):
    with get_db_connection() as connection:
        connection.execute(
            'DELETE FROM students WHERE id_number = ?',
            (id_number,)
        )

# ==========================================
# TEACHER CRUD FUNCTIONS
# ==========================================

def add_teacher(name, email, department, office_room, employee_id):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO teachers (name, email, department, office_room, employee_id) VALUES (?,?,?,?,?)',
            (name, email, department, office_room, employee_id),
        )

def get_teachers():
    with get_db_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()

def update_teacher(employee_id, name, email, department, office_room):
    with get_db_connection() as connection:
        connection.execute(
            '''UPDATE teachers
                SET name = ?, email = ?, department = ?, office_room = ?
                WHERE employee_id = ?''',
            (name, email, department, office_room, employee_id)
        )

def delete_teacher(employee_id):
    with get_db_connection() as connection:
        connection.execute(
            'DELETE FROM teachers WHERE employee_id = ?',
            (employee_id,)
        )

# ==========================================
# COURSE CRUD FUNCTIONS
# ==========================================

def add_course(course_code, title, credit, semester, teacher_id):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO courses (course_code, title, credit, semester, teacher_id) VALUES (?,?,?,?,?)',
            (course_code, title, credit, semester, teacher_id),
        )

def get_courses():
    with get_db_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()

def update_course(course_code, title, credit, semester, teacher_id):
    with get_db_connection() as connection:
        connection.execute(
            '''UPDATE courses
                SET title = ?, credit = ?, semester = ?, teacher_id = ?
                WHERE course_code = ?''',
            (title, credit, semester, teacher_id, course_code)
        )

def delete_course(course_code):
    with get_db_connection() as connection:
        connection.execute(
            'DELETE FROM courses WHERE course_code = ?',
            (course_code,)
        )














































# import sqlite3
# from contextlib import contextmanager

# sqlite_file_name="school.db"

# @contextmanager
# def get_db_connection():
#     connection=sqlite3.connect(sqlite_file_name)

#     connection.row_factory = sqlite3.Row
#     try:
#         yield connection
#         connection.commit()
#     finally:
#         connection.close()

# def create_table():
#     with get_db_connection() as connection:
#         connection.execute('''CREATE TABLE IF NOT EXISTS students(
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         name TEXT NOT NULL,
#                         age INTEGER NOT NULL,
#                         email TEXT NOT NULL,
#                         country TEXT NOT NULL,
#                         id_number INTEGER NOT NULL
#                         )''' )

# def add_student(name, age, email, country, id_number):
#     with get_db_connection () as connection:
#         connection.execute(
#         'INSERT INTO students (name, age, email, country, id_number) VALUES (?,?,?,?,?)',
#             (name, age, email, country, id_number),
#             )
    
# def get_student():
#     with get_db_connection() as connection:
#         return connection.execute('SELECT*FROM students').fetchall()

# def update_student(id_number, name, age, email, country):
#     with get_db_connection() as connection:

#         connection.execute(
#             '''UPDATE students
#                 SET name = ?, age = ?, email = ?, country = ?
#                 WHERE id_number = ?''',
#                 (name, age, email, country, id_number)
#                 )
#         connection.commit()

# def delete_student(id_number):
#     with get_db_connection() as connection:

#         connection.execute(
#         'DELETE FROM students WHERE id_number = ?',
#         (id_number,)
#         )
#         connection.commit()