'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-09 21:35:47
LastEditors: CoderXZ
LastEditTime: 2021-05-09 21:37:15
'''
def counter():
    i = 0
    while True:
        i += 1
        yield i
def inc(c):
    return next(c)

c = counter()
print(inc(c))
print(inc(c))