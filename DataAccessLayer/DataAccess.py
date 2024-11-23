import sqlite3
from CommonLayer.User import User

class DataAccess:
    def get_user(self,username,password):
        print("getuser1")
        with sqlite3.connect("C:/Users/Arta/Desktop/projects/project1/DataAccessLayer/database.db") as connection:
            cursor = connection.cursor()
            data = cursor.execute("""SELECT id,
       Name,
       Lname,
       username,
       password,
       National_code,
       Class
  FROM Students
  where username = ?
  and password = ?;

  
""",[username,password])
            print(data)
            #user = User(data[0],data[1],data[2],data[3],None,data[5],data[6])
            # print(f"Data Access is working Hello {user.fName} {user.lName}")
            # return user