# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 02:16:07 2019

@author: niili

На вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на 
строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции
строка s перейдет в строку "baba", после выполнения двух и операций – в строку 
"bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s не 
останется вхождений строки a. Если операций потребуется более 1000, выведите 
Impossible.

Выведите одно число – минимальное число операций, после применения которых в 
строке s не останется вхождений строки a, или Impossible, если операций 
потребуется более 1000.

"""

"""
At first, check is there string a in string s. If not, print "Impossible", else
check is there string a in b. If yes, then replace be infinity, print 
"Impossible". Else we have a while loop. Until string a in string s and counter
of operation < 1000, replace string a to string b.
"""

s = input()
a = input()
b = input()

if a not in s:
    print(0)
elif a in b:
    print("Impossible")
else:
    i = 0
    while ((a in s) or (i > 1000)):
        s = s.replace(a,b)
        i += 1
    if i < 1000:
        print(i)
    else:
        print("Impossible")