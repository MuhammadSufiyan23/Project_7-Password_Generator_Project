# PROJECT: 7
# PASSWORD GENERATOR PROJECT

import random
import string

def password_generator(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

length = int(input("🔢 Enter the Length of Your Desired Password 🔐: "))
password = password_generator(length)
print("\n✅ Your Secure Generated Password: 🔑", password)
