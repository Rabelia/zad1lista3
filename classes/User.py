import hashlib
from classes.Exceptions import *  # importuje klase wyjatkow
from classes.Editor import *


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(password)  # zenkryptowane haslo
        self.is_logged = False

    def _encrypt_password(self, password):
        tmp_passwd = f"{self.username}:{password}"
        encrypted_passwd = hashlib.sha256(str(tmp_passwd).encode('utf-8'))  # enkrypcja hasla
        return encrypted_passwd

    def check_password(self, password):
        tmp_passwd = f"{self.username}:{password}"
        if hashlib.sha256(str(tmp_passwd).encode(
                'utf-8')).hexdigest() == self.password.hexdigest():  # hexdigest wyswietla "szyfr"
            return True
        else:
            return False


class Authenticator:
    def __init__(self):
        self.users = {}  # pusty slownik

    def add_user(self, user):
        try:
            if user.username in self.users:
                raise UsernameAlreadyExists

            self.users[user.username] = user
            print(f"Dodano użytkownika o nazwie {user.username} do słownika użytkowników")

        except UsernameAlreadyExists as error:
            print(error)

        except PasswordTooShort:
            print("Podane hasło jest za krótkie, wpisz hasło zawierające co najmniej 7 znaków.")

    def login(self, username, password):
        tmp_passwd = f"{username}:{password}"
        if not hashlib.sha256(str(tmp_passwd).encode(
                'utf-8')).hexdigest() == self.users[username].password.hexdigest():  # hexdigest wyswietla "szyfr"
            self.users[username].is_logged = True
            print(f"Logowanie użytkownimka {username} powiodło się")
        else:
            raise IncorrectUsername()


    def is_logged_in(self, user):
        if user.is_logged is True:
            print(f"Użytkownik {user.username} zalogowany")
            return True
        else:
            print(f"Użytkownik {user.username} niezalogowany")
            return False


class Authorizor():
    def __init__(self, authenticator):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self, permission):
        try:
            self.permissions[permission] = set()

        except PermissionError as error:
            print(error)

    def permit_user(self, user, permission):
        try:
            self.permissions[permission] = user

        except PermissionError as error:
            print(error)

        except IncorrectUsername as error:
            print(error)

    def check_permission(self, user, permissions):
        try:
            permissions == user
        except PermissionError as error:
            print(error)