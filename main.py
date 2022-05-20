from Exceptions import *
from User import *
from Editor import *


user1 = User("mbochenek", "haslo")
user2 = User("kdrzewiecka", "password")
user3 = User("pfryzlewicz", "test")
user_list = Authenticator()
permision_list = Authorizor(user_list)

user_list.add_user(user1)
user_list.add_user(user2)
user_list.add_user(user3)

permision_list.add_permission("admin")
permision_list.add_permission("moder")

permision_list.permit_user(user_list.users['mbochenek'], 'admin')
permision_list.permit_user(user_list.users['kdrzewiecka'], 'admin')
permision_list.permit_user(user_list.users['pfryzlewicz'], 'moder')

print(permision_list.permissions['admin'].username)
print(permision_list.permissions['moder'].username)

editor = Editor()

editor.login(user_list)