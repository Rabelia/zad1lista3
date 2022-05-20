from classes.User import *
from classes.Exceptions import *


class Editor:
    def __init__(self):
        self.user_name = None
        # self.options = {"a": self.login(), "b": self.test(), "c": self.change(), "d": self.quit()}

    def login(self, user_list):
        username = input("Podaj nazwę użtykownika: ")
        password = input("Podaj hasło: ")
        user_list.login(username, password)

    def is_permitted(self):
        pass

    def test(self):
        pass

    def change(self):
        pass

    def quit(self):
        pass

    def run(self):
        # print("Podaj Klucz:")
        # key = input()
        pass
