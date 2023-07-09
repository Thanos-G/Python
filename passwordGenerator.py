import random
import string

def genarate_password(length):
    password = ""
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

password_length = int(input('Enter the desired length for the password: '))
password = genarate_password(password_length)
print('Generated password: ', password)
