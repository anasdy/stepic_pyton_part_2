# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:32:12 2019

@author: niili

Программа отвечает на запросы яявляется ли один класс предком другого.
Создавать классы не требуется.

Класс A является предком класса B, если

    A = B;
    A - прямой предок B
    существует такой класс C, что C - прямой предок B и A - предок C

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке 
указано от каких классов наследуется i-й класс. Обратите внимание, что класс 
может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам 
от себя (прямо или косвенно), что класс не наследуется явно от одного класса 
более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> 
<имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 
50.

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 
является предком класса 2, и "No", если не является. 



Пример воода:
4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A


Пример вывода:
Yes
Yes
Yes
No


Структура наследования классов хорошо представляется графом, в python граф 
удобно представлять списками и матрицами смежности, либо использовать готовые 
библиотеки. 
Я попробую два варианта решения:   
    1 - самостоятельная реализация, 
    2 - использование библиотеки python-graph 
        (https://github.com/Shoobx/python-graph)

Вариант1.
Данное решение - вариант списков смежности.
Структура данных: словарь. Где ключ - имя класса, значение - список предков.
Поиск предков осуществляется рекурсивной функцией.


"""
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Функуция определения является класс 1 предком класса 2.
# Класс A является предком класса B, если
#   A = B;
#   A - прямой предок B
#   существует такой класс C, что C - прямой предок B и A - предок C
# Аргументы функции:
# clss_1 - Имя класса 1, предполагаемого предка, тип str
# clss_2 - Имя класса 2, предполагаемого потомкаб тип str
# class_tree_dict - Ссылка на словарь, тип dict

# Возвращаемое значение
# True - если класс 1 является предком класса 2.
# False - в противном случае

# Если у класса 2 нет предков, возвращаем False
# Если класс 1 в списке предков класса 2, возвращаем True
# Иначе - запустить функциюдля каждого класса из списка предков класса 2.
#       Если хоть одно из возвращаемых значений True, возвращаем True.
#---------------------------------------------------------

def f_class_parents_test(clss_1, clss_2, clss_tree_dict):
    # если класс1 и класс2 одинаковые - ответ положительный
    if clss_1 == clss_2:
       return True
    # Если у класса 2 нет предков, возвращаем False
    elif clss_tree_dict[clss_2]:
        return False
    # Иначе проверяем есть ли класс1 в списке предков класса2
    elif clss_1 in clss_tree_dict[clss_2]:
        return True
    # Если нет, проверяем есть ли класс1 в списке предков
    # одного из предков класса2
    else:
        for clss in clss_tree_dict[clss_2]:
            if f_class_parents_test:
                return True     #!!!!! проверить необходимое количество return!
            else:
                continue        # else вроде необязателен, но так нагляднее
        # если мы дошли сюда, значит класс1 не предок класса2 и ни одного
        # из его предков
        return False


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# считать количество классов
n_clss = int(input())
# завести словарь,
# в цикле считывать имя класса как ключ,
# список его предков как значение
clss_tree_dict = dict()
for i in range(n_clss):
    clss_name = input()
    if ':' in  clss_name:
        clss_name, clss_parents = input().split(":")
        clss_parents = clss_parents.split()
    else:
        clss_parents = []
    clss_tree_dict[clss_name] = clss_parents
#---------------------------------------------------------
    
# считать количество запросов
n_requests = int(input())
# в цикле считать запрос
for i in range(n_requests):
    clss_1, clss_2 = input().split()
    # если они разные - запустить функцию поиска, вывести ответ на экран
    if f_class_parents_test(clss_1, clss_2, clss_tree_dict):
        print('Yes')
    else:
        print('No')
    





































