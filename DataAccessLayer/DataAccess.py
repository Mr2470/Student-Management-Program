import sqlite3


class DataAccess():
    # controls needed commands for the database

    def initialize(database_file):
        # creates table named "students" if it doesn't exist

        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS students (fName text, lName text, username text, password text)")

            connection.commit()
            print("Database initialization complete")

    def insert_student(database_file, fName, lName, username, password):
        # checks the database and adds student

        if DataAccess.get_student(database_file, username) != None:
            print("ERROR: username already exists")
            return

        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()

            cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (fName, lName, username, password))

            connection.commit()


    def get_student(database_file, username):
        # returns student with specific username

        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()

            cursor.execute("""SELECT * FROM students WHERE username=?""", (username,))
            st = cursor.fetchone()

            print("student:")
            print(st)

            connection.commit()
            return st;


    def get_students(database_file):
        # returns all students in the table

        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT rowid,* FROM students")
            students = cursor.fetchall()

            for st in students:
                print(st);

            connection.commit()
            return st
    
    def delete_student(database_file, username):
        # deletes student with specific username

        with sqlite3.connect(database_file) as connection:
            cursor = connection.cursor()

            cursor.execute("DELETE FROM students WHERE username=?", (username,))

            connection.commit()

