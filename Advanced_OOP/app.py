from admin import Admin
from database import Database


a = Admin('rolf', '1234', 3)
u = User('jose', 'password')

a.save()

print(Database.find(lambda x : x['username'] == 'rolf'))

users = [a, u]
for user in users:
    user.save()


