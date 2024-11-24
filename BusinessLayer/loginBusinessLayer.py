from DataAccessLayer.DataAccess import DataAccess

class Login:
    def __init__(self):
        self.data_access_layer = DataAccess
    def check_username_password(self,username, password):
        print(username,password)
        UserDataAccess = DataAccess()
        user = UserDataAccess.get_student(username,password)