# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 13:25:19 2019

@author: niili

Реализуйте программу, которая будет эмулировать работу с пространствами имен. 
Необходимо реализовать поддержку создания пространств имен и добавление в них 
переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый 
идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

    create <namespace> <parent> –  создать новое пространство имен с именем 
                                    <namespace> внутри пространства <parent>
    add <namespace> <var> – добавить в пространство <namespace> переменную
                            <var>
    get <namespace> <var> – получить имя пространства, из которого будет взята 
                            переменная <var> при запросе из пространства 
                            <namespace>, или None, если такого пространства не 
                            существует

Формально, результатом работы get <namespace> <var> является <namespace>, если 
в пространстве <namespace> была объявлена переменная <var> get <parent> <var> –
результат запроса к пространству, внутри которого было создано пространство 
<namespace>, если переменная не была объявлена None, если не существует 
<parent>, т. е. <namespace>﻿ – это global
    
Формат входных данных

В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
В каждой из следующих n строк дано по одному запросу.
Запросы выполняются в порядке, в котором они даны во входных данных.
Имена пространства имен и имена переменных представляют из себя строки длины 
не более 10, состоящие из строчных латинских букв.

Формат выходных данных

Для каждого запроса get выведите в отдельной строке его результат.

---------------------------------------------------------------------

В качествеструтуры данных выберем словарь:
    ключ        -   название пространства имен
    значение    -   массив [<name>, <parent>, <var_list>], где <name> - имя 
                    пространства имен <parent> ссылка на пространство, внутри 
                    которого находится данное (для global это значение None),  
                    а <var_list> - список переменных в этом пространстве имен.
                    
Такая структура позволит обеспечить достаточно быстрый доступ к данным, а 
хранине и обход смежных вершин, которое могло бы требовать другой структуры 
данных в данной задаче не нужно.

Кроме того, не оговорена реакция на добавление нового пространсва имен с 
несуществующим предком, переменной в несуществующее пространство имен, как и на
не существующий запрос.
Так как это учебная задача, тестируемая через стандартный ввод-вывод из 
возможных действий : не обрабатывать ошибку, обработать и вывести на экран 
сообщение об ошибке, оббработать, но сообщение не выводить, выбран последний 
вариант. В случае отстутвия родительского пространсва имен- новое будет 
создаваться в global.

Возможны два варианта реализации программы: написать отдельные функции и 
вызвывать их в зависимости от запроса или написать код реализации прямо в цикле
основной программы. Первый способ нагляднее и больше подходит для внесения 
дальнейших изменений.
"""
#------------------------------------------------------------------------------
#_create
#------------------------------------------------------------------------------
# Function add new namespace in namespaces list.

# Input
# namespaces_dict - dictionary
#                       key - name of namespace
#                       value - [<point to parent namespace>, [list of var]]
# new_namespace_name - name of new namespace
# parent_name - name of parent namespace
#------------------------------------------------------------------------------
def create(namespaces_dict, new_namespace_name, parent_name):
    # if parent namespace not in namespaces_list - create new namespase in 
    # global
    if parent_name not in namespaces_dict: 
        parent_name = 'global'
    namespaces_dict[new_namespace_name] = [new_namespace_name, namespaces_dict[parent_name], []]
    return

#------------------------------------------------------------------------------
#_add
#------------------------------------------------------------------------------
# Function add new variable in namespace.

# Input
# namespace - point to value of dictionary veiw [<point to parent namespace>, 
#             [list of var]]
# var_name - name of new variable
#------------------------------------------------------------------------------
def add(namespace, var_name):
    namespace[2].append(var_name)
    return

#------------------------------------------------------------------------------
#_get
#------------------------------------------------------------------------------
# Function return name of namespace from wich we get the var if refer to 
# variable from this namespace
    
# Input
# namespace - namespace from refer the var, point to value of dictionary veiw 
#             [<point to parent namespace>, [list of var]]
# var_name - name the refer var


#------------------------------------------------------------------------------
def get(namespace, var_name):
    # if var in var_list
    if var_name in namespace[2]:
        return namespace[0]
    # or we in global and haven't var
    elif namespace[0] == 'global':
        return 'None'
    # else - look at parent namespace
    else:
        return get(namespace[1], var_name)


#------------------------------------------------------------------------------
#_main
#------------------------------------------------------------------------------

# number of instruction
n_instr = int(input())


# list of namespaces
# in start namespaces list have only 'global', which haven't parent and haven't
# variable at this point
namespaces_dict = {'global' : ['global', None, []]}

# read n instruction
for i in range(n_instr):
    # read line and split on instuction, namespace and name of variable or 
    # parent namespace
    instr, namespace, name = input().split()
    
    if instr == 'create':
       create(namespaces_dict, namespace, name)
    elif instr == 'add':
        # if this namespace create - add var
        if namespace in namespaces_dict:
            add(namespaces_dict[namespace], name)
        # else - do nothing
    elif instr == 'get':
        print(get(namespaces_dict[namespace], name))













































