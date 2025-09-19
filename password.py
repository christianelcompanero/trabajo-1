import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input('ingresa la longitud de tu password'))
password = ""

for i in range(longitud):
    password += random.choice(caracteres)

print("tu password nuevo es:", password)
