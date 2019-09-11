# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:35:39 2019

@author: niili

Файл для маленьких заданий. И кода из лекций

"""

#------------------------------------------------------------------------------

"""
# 1.1
fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31))
"""

#------------------------------------------------------------------------------

# 1.2 objects id

"""
x = [1, 2, 3]
print(id(x))
print(id([1, 2, 3])) # it is different lists!
"""
"""
x = [1, 2, 3]
y = x
print(y is x)
#print(y is [1, 2, 3])
x.append(4)
print(x)
print(y)
"""
#------------------------------------------------------------------------------
"""
# 1.2 objects types

x = [1, 2, 3]
print(type(x))
print(type(5))

print(type(type(x)))
"""

#------------------------------------------------------------------------------
"""
# 1.3 small closest mod 5 function

def closest_mod_5(x):
    while(x % 5 != 0):
        x += 1
    return x
   """ 
#------------------------------------------------------------------------------   
"""
class A:
    val = 1
    
    def foo(self):
        A.val += 2
    
    def bar(self):
        self.val += 1


a = A()
b = A()

print('a = ', a.val)
print('b = ', b.val)
a.bar()
print('a = ', a.val)
print('b = ', b.val)
a.foo()
print('a = ', a.val)
print('b = ', b.val)
c = A()
print(a.val)
print(b.val)
print(c.val)
"""
#------------------------------------------------------------------------------
class Song:
    
    def __init__ (self, artist, song):
        self.artist = artist
        self.song = song
        self.tags = []
        
    def add_tags(self, *args):
        print(args)
        self.tags.extend(args)
        
        
        
song1 = Song("aaa", "bbbb")
song1.add_tags("Americana", "Country")


song2 = Song("bbbb", "ccccccccccc")
song2.add_tags("Russian", "Rock")

print(song2.tags)







