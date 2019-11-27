# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:58:12 2019

@author: niili

Вам дана в архиве файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой 
структуре все директории, в которых есть хотя бы один файл с расширением ".py". 

Ответом на данную задачу будет являться файл со списком таких директорий, 
отсортированных в лексикографическом порядке.

"""

import os.path


py_dir_list = []
# walk in directory
for current_dir, dirs, files in os.walk("./main"):
    # look at all files
    for file in files:
        # look to file extension
        # if this is .py-file
        n = len(file)
        if file[n - 3: n] == ".py":
            # cut ./, add in list, exit from loop
            py_dir_list.append(current_dir[2:])
            break

# sort in lexicographical order
py_dir_list.sort()
    
# write in file
with open("2_4_2_answer.txt", "w") as f:
    for dir_el in py_dir_list:
        dir_el = dir_el + "\n"
        f.write(dir_el)