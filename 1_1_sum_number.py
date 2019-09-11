# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:43:02 2019

@author: niili

Программа принимает последовательность чисел и выводит их сумму.
на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.

Выведите одно число – сумму данных n чисел.


"""

# read number of lines
n_lines = int(input())

sum_numb = 0

# read the numbers and calculate sum
for i in range(n_lines):
    numb = int(input())
    sum_numb += numb
print(sum_numb)