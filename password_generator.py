num = int(input("Number of passwords: "))
length = int(input("Password length: "))

num = int(num)
length = int(length)

import random

chars = 'abcdefghijklmnopqrstuvwqyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,./<>?@[]{}~'


for p in range(num):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)