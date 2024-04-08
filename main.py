import os
from functools import reduce

def create_file(file_name):
    try:
        with open(f'{file_name}.txt', 'w') as file:
            file.write('Id\tIsm\tFamiliya\tTelefon\tEmail\tPassword')
            return True
    except FileExistsError as arr:
        print(arr)
        return False

while True:
    if os.path.exists('users.txt'):
        break
    file_name = input('Fayl nomini kiriting (users deb kiriting): ')
    if file_name == 'users':
        if create_file(file_name):
            print('Fayl ochildi')
            break
    else:
        print('users deb kiriting!')

def generate_id():
    with open('users.txt') as file:
        return len(file.readlines())

def register():
    ism = input('Ism: ')
    familiya = input('Familiya: ')
    telefon = input('Telefon: ')
    email = input('Email: ')
    while True:
        password = input('password1: ')
        password2 = input('password2: ')
        if password == password2:
            print('Ro\'yxatdan muvoffaqqiyatli o\'tdingiz')
            break
        else:
            print('Prolingiz mos kelmadi qayta kiriting!')
    with open('users.txt', 'a') as file:
        file.write(f'\n{generate_id()}\t{ism}\t{familiya}\t{telefon}\t{email}\t{password}')

while True:
    if 'ha' == input('ro\'yxatdan o\'tasizmi? ha/yo\'q: ').lower():
        register()
    else:
        break

def str_sum(str1, str2):
    return str1 + f'{(3 - len(str1)) * " "}' + ' | ' + str2.replace('\n', '') + f'{(20 - len(str2)) * " "}'

def show_users():
    with open('users.txt') as file:
        data = file.readlines()
        info = str()
        for line in data:
            line = line.split('\t')
            info += reduce(str_sum, line) + '\n'
        print(info)
show_users()

def show_user(user_id):
    with open('users.txt') as file:
        data = file.readlines()
        try:
            data = data[0], data[user_id]
        except IndexError:
            info = 'Bunday id li user yo\'q'
        else:
            info = str()
            for line in data:
                line = line.split('\t')
                info += reduce(str_sum, line) + '\n'
        return info

while True:
    try:
        user_id = int(input('Id ni kiriting: '))
    except ValueError:
        print('Id ni noto\'g\'ri kiritdingiz qayta kiriting!')
    else:
        break

print(show_user(user_id))
