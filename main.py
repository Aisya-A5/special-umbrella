import random

keyword = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

password = ''

pw_length = int(input('masukan panjang password'))

for i  in range(pw_length):
    password += random.choice(keyword)

print(password)
