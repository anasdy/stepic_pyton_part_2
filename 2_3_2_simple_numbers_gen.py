# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 02:32:53 2019

@author: niili


Реализуйте функцию-генератор primes, которая будет генерировать простые числа в
порядке возрастания, начиная с числа 2.
"""

def primes():
    # идем перебором от 2
    i = 1
    while True:
        i += 1
        is_simple = f_is_simple_number_function(i)
        if is_simple:
            yield i
        # если нет, переходим к следующему i
        else:
            continue
        
    
    
    
def f_is_simple_number_function(x): 
    # Проверка является ли число простым
    # взяла метод перебора делителей
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
    

   

gen = primes()
for j in range(3):
    print('j = ', j)
    print('primes = ', next(gen))