# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 08:14:42 2020

@author: niili


Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри
A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из
 A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и
 B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на
существующие HTML документы.

"""
#------------------------------------------------------------------------------

import requests
import lxml.html



#------------------------------------------------------------------------------
# read A and B URL
a_url = input()
b_url = input()

# get A
list_links = []
res_a = requests.get(a_url)
if res_a.status_code != 200:
    print("Error open URL ", a_url, "with code ", res_a.raise_for_status())
else:
    # parsed html
    parsed_a = lxml.html.fromstring(res_a.text)
    # find links with xpath (look xml)
    # //a - find all tag a
    # //a/href - find all element href, wich have parent is a-tag
    # @href - find atribute, value of href-tag
    print(parsed_a.xpath('//a/@href'))
    #list_links.append
