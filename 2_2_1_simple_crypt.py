# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:58:26 2019

@author: niili

Даны 2 файла.
Первый - бинарный, содержит информацию, зашифрованную при помощи метода 
simplecrypt.encrypt.

Второй хранит пароли в открытом виде.

Необходимо с помощью метода simplecrypt.decrypt узнать, какой из паролей служит
ключом для расшифровки файла с информацией.

Ответом служит расшифрованная информация

"""

import simplecrypt


# open first file with information
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

    # open second file with passwords
    with open("passwords.txt", 'r') as passw:
        for line in passw:
            line = line.rstrip()
            # use decrypt with each password and print result
            print(line)
            try:
                print(simplecrypt.decrypt(line, encrypted))
            except simplecrypt.DecryptionException:
                print("This Password not so good")