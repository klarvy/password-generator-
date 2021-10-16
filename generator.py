import random 

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = input('Сколько надо паролей:'+ "\n")

dlina = input("Длину пароля:"+ "\n")

number = int(number)

dlina = int(dlina)

for n in range(number):

    password = ''

    for i in range(dlina):

        password += random.choice(chars)

    print(password)

    file = open( "password.txt", 'a')

    file.write( "\n" + password )

    file.close()
