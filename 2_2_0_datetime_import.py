# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:23:57 2019

@author: niili

В первой строке дано три числа, соответствующие некоторой дате date -- год, 
месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента 
исходной даты date пройдет число дней, равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.

"""

import datetime

# read data
year, month, day = [int(x) for x in input().split()]
date = datetime.date(year, month, day)

# read number of days
n_days = int(input())
# n_days from int to date
delta = datetime.timedelta(days = n_days)
# calc new date
date = date + delta
# print date in format YYYY M D without 0.
# For win-systems use #m #d
# For unix systems use -m -d
print(date.strftime("%Y %#m %#d"))
                    
# Interestingly, how write this code with check OS automaticly