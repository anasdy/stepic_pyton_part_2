# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 01:56:36 2019

@author: niili


Реализовать рекурсивное вычисление числа сочетаний из n по k.
Вход: строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
Выход: единственное число: C(n, k).

"""
#------------------------------------------------------------------------------

def c_n_k(n, k):
    if k > n:
        return 0
    elif k == 0 or k == n:
        return 1
    else:
        return c_n_k(n - 1, k) + c_n_k(n - 1, k - 1)

#------------------------------------------------------------------------------

# read n and k
n, k = map(int, input().split())

print(c_n_k(n, k))