import random
n = int(input("Enter the lenth of the password: "))
m = int(input("How many passwords to generate?: "))
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-.,<>/?|'

for d in range(m):
    password = ''
    for c in range (n):
        password += random.choice(chars)
    print(password)
