import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(){},?"

def pwd_generator():
    len_pass = input("Input your password length: ")
    try:
        len_pass = int(len_pass)
    except:
        print('<Error> Length should be a number !!')
        pwd_generator()

    print("::: Passwords :::\n")
    for pwd in range(7):
        passwords = ""
        for c in range(len_pass):
            passwords += random.choice(chars)
        print(passwords)

pwd_generator()
