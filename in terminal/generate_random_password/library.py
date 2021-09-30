import random
import string

def generate_random_password(length):
    allCharacter = string.ascii_letters + "123456789/*-+!@#$%^&*()"
    password = ''
    for i in range(1, length + 1):
        rand = random.randint(0, len(allCharacter) - 1)
        password = password + allCharacter[rand]
    print(password)
