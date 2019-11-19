# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 02:32:53 2019

@author: niili


Реализуйте функцию-генератор primes, которая будет генерировать простые числа в
порядке возрастания, начиная с числа 2.
"""

def primes():
    # идем перебором от 2
    while True:
        print('primes generator')
        i = 2
        # проверяем на простоту
        if f_is_simple_function(i):
            # если простое - возвращаем его
            yield i
        # если нет, переходим к следующему
    
    
    
def f_is_simple_function(x): 
    # Проверка является ли число простым
    # взяла метод перебора делителей
    print("is isimple function")
    for i in range(2,x):
        print(i)
        if x % i == 0:
            return False
    return True
    



for i in range(5):
    res = primes()
    print('primes:', res)