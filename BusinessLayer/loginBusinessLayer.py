from DataAccessLayer.DataAccess import DataAccess

class Login:
    def __init__(self):
        self.data_access_layer = DataAccess
    def check_username_password(self,username, password):
        print(username,password)
        UserDataAccess = DataAccess()
        user = UserDataAccess.get_user(username,password)
arta = Login()
print(arta.check_username_password("test","123123"))