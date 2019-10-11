# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:19:22 2019

@author: niili

Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable 
таким образом, чтобы при добавлении элемента в список посредством метода append
в лог отправлялось сообщение, состоящее из только что добавленного элемента.

класс Loggable:

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

"""

class LoggableList(list, Loggable):
    
    def append(self, el):
        super(LoggableList, self).append(el)
        self.log(el)