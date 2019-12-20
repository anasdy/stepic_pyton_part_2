# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 01:03:37 2019

@author: niili
"""

import re


"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
"""



#import sys

pattern = r".*(cat).*\1.*"

#for line in sys.stdin:
#    line = line.rstrip()
    

line = input().rstrip()
match_object = re.search(pattern, line)
print(re.search(pattern, line).__doc__)

# паттерн, кажется, правеильный. Как сделать проверку пока не поняла (как достать результат search)