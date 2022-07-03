import hashlib
from classes.Exceptions import *  # importuje klase wyjatkow
from classes.Editor import *


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(password)
        self.is_logged = False

    def _encrypt_password(self, password):
        tmp_passwd = f"{self.username}:{password}"
        encrypted_passwd = hashlib.sha256(str(tmp_passwd).encode('utf-8'))
        return encrypted_passwd

    def check_password(self, password):
        tmp_passwd = f"{self.username}:{password}"
        if hashlib.sha256(str(tmp_passwd).encode(
                'utf-8')).hexdigest() == self.password.hexdigest():
            return True
        else:
            return False


class Authenticator:
    def __init__(self):
        self.users = {}  # pusty slownik

    def add_user(self, user): #USER ALREADY EXIST ERROR DO POPRAWY BO NIE DZIAŁA (NA DOLE MOŻESZ TESTOWAĆ DODAWANIE USERÓW)
        try:
            if user.username in self.users:
                raise UsernameAlreadyExists

            self.users[user.username] = user

        except UsernameAlreadyExists as error:
            print(error)

        except PasswordTooShort as error:
            print(error)

    def login(self, username, password): # PASSWORD TOO SHORT I ZŁY USERNAME DODAĆ BO NIE MA :C
        tmp_passwd = f"{username}:{password}"
        if hashlib.sha256(str(tmp_passwd).encode(
                    'utf-8')).hexdigest() == self.users[
            username].password.hexdigest():
            self.users[username].is_logged = True
            print(f"Logowanie użytkownika {username} powiodło się")
        else:
            print(f"Logowanie {username} nie powiodło się. Błędny login lub hasło")
            quit()

    def is_logged_in(self, user): # AUTHENTICATION ERROR CZY JAOŚ TAK - W SENSIE ŻE NIE JEST ZALOGOWANY
        if self.users[
            user].is_logged is True:
            return True
        else:
            raise NotPermittedError


class Authorizor():
    def __init__(self, authenticator):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self, permission):
        self.permissions[permission] = set()

    def permit_user(self, user, permission):
        self.permissions[permission].add(user)

    def check_permission(self, user, permission):  # NIE MA SPRAWDZACZA, CZY UPRAWNIENEI ISTNIEJE
        if user in self.permissions[permission]:
            return True
        else:
            return False


user1 = User("mbochenek", "haslo")
user2 = User("kdrzewiecka", "password")
user3 = User("pfryzlewicz", "test")
user4 = User("pfryzlewicz", "test")
user_list = Authenticator()
permision_list = Authorizor(user_list)

user_list.add_user(user1)
user_list.add_user(user2)
user_list.add_user(user3)
user_list.add_user(user4)

permision_list.add_permission("admin")

permision_list.permit_user("mbochenek", "admin")
permision_list.permit_user("kdrzewiecka", "admin")
permision_list.permit_user("pfryzlewicz", "admin")