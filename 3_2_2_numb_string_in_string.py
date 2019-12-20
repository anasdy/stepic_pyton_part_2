# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 02:40:15 2019

@author: niili

На вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa

"""

"""
Check is there string t in s. If not - print 0. Else: Find index of first 
occurences, memorize it, find next occurences from memorize index. Adn do it 
until we find no occurences.
"""

s = input()
t = input()

if t not in s:
    print(0)
else:
    flag = True
    index = 0 
    i = 0
    while flag:
        new_index = s.find(t, index)
        if new_index == -1 :
            flag = False
        else:
            index = new_index + 1
            i += 1
    print(i)
            