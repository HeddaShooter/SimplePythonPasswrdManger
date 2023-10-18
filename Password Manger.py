import os
import random
import string

chars = string.ascii_letters + string.digits + '!@#$%&()'

Where = input("Type in where the login is for: ")
print(Where)
Username = input("What is your username for the login: ")
print(Username)
CharAmount = int(input("How many characters do you want the password to be?: "))
print(CharAmount)

genPass = ''.join(random.choice(chars) for i in range(CharAmount))
print(genPass)

with open('logins.txt', 'a') as file:
    file.write('Login for: ' + Where + '\n')
    file.write('Username: ' + Username + '\n')
    file.write('Password: ' + genPass + '\n')
    file.write('-----------------------------------\n')
