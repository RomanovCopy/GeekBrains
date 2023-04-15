import random
import string

def generatorPassword(length):
    letters_and_digits = string.ascii_letters + string.digits
    password = ''.join(random.sample(letters_and_digits, length))
    return password

print(generatorPassword(int(input("Key length : "))))
