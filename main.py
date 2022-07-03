from classes.Exceptions import *
from classes.Authorization import *
from classes.Editor import *


def menu():
    edit = Editor()
    while True:
        edit.run()


if __name__ == '__main__':
    menu()
