import sqlite3
from math import trunc

from CommonLayer.User import User


class DataAccess:
    def get_student(self, username, password):
        # returns student with specific username

        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()

            cursor.execute("""SELECT * FROM students WHERE username=? and password = ?""", (username, password))
            st = cursor.fetchone()

            print("student:")
            print(st)

            connection.commit()
            try:
                user = User(st[0], st[1], st[2], st[3], None, st[5], st[6])
                print(f"user Successfully Created {user.fName} {user.lName} {user.username}")

            except:
                raise Exception("Incorrect username or password")
            else:
                return user

    def get_students(self):
        # returns all students in the table

        with sqlite3.connect("./database.db") as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT rowid,* FROM students")
            students = cursor.fetchall()

            for st in students:
                print(st)

            connection.commit()
            return st

    def delete_student(self, username):
        # deletes student with specific username

        with sqlite3.connect("./database.db") as connection:
            cursor = connection.cursor()

            cursor.execute("DELETE FROM students WHERE username=?", (username,))

            connection.commit()

    # controls needed commands for the database

    # def initialize(database_file):
    #    # creates table named "students" if it doesn't exist
#
#    with sqlite3.connect(database_file) as connection:
#        cursor = connection.cursor()
#
#        cursor.execute("CREATE TABLE IF NOT EXISTS students (fName text, lName text, username text, password text)")
#
#        connection.commit()
#        print("Database initialization complete")

# def insert_student(database_file, fName, lName, username, password):
#    # checks the database and adds student
#
#    if DataAccess.get_student(database_file, username) != None:
#        print("ERROR: username already exists")
#        return
#
#    with sqlite3.connect(database_file) as connection:
#        cursor = connection.cursor()
#
#        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (fName, lName, username, password))
#
#        connection.commit()
#
