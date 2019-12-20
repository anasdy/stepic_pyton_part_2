# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:56:23 2019

@author: niili

Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда 
функцию от одного аргумента y, которая будет возвращать True, если остаток от 
деления y на x равен mod, и False иначе.

"""

def mod_checker(x, mod=0):
    return lambda y: y % x == mod 