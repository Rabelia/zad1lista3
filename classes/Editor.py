from classes import Authorization
from classes.Exceptions import *
from classes.Authorization import *


class Editor:
    def __init__(self):
        self.username = None
        self.options = {
            "a": self.login,
            "b": self.test,
            "c": self.change,
            "d": self.quit,
            "e": self.is_permitted}

    def login(self):
        if Authorization.user_list.is_logged_in(self.username):
            print("Użytkownik zalogowany.")
        else:
            password = input("Podaj hasło: ")
            try:
                Authorization.user_list.login(self.username, password)
            except IncorrectUsername as error:
                print(error)
            except IncorrectPassword as error:
                print(error)

    def is_permitted(self, permission):
        if Authorization.user_list.is_logged_in(self.username):
            if Authorization.permision_list.check_permission(self.username, permission):
                return True
            else:
                return False
        else:
            Editor.login(self)

    def test(self):
        if not Editor.is_permitted(self, "admin"):
            print("Brak uprawnień")
        else:
            # program coś tu robi
            print("Wszystko git")
            pass

    def change(self):
        pass

    def quit(self):
        quit()

    def run(self):
        if self.username is None:
            self.username = input(
                "Podaj nazwę użytkownika: ")  # TRY CZY UŻYTKOWNIK ISTNIEJE ALE NIEKONIECZNIE BO TO SAMO BĘDZIE SPRAWDZANE PRZY LOGINIE
            if self.username in Authorization.user_list.users:
                    print("---------MENU OPCJI---------")
                    print("[a] - Login")
                    print("[b] - Test")
                    print("[c] - Change")
                    print("[d] - Exit")
                    choice = input("Wybierz opcje: ")
                    if not choice in self.options:
                        print("Nie ma takiej opcji!")
                    else:
                        self.options[choice]()
            else:
                IncorrectUsername()
                self.quit()
