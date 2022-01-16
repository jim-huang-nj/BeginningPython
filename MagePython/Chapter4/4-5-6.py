'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-09 21:39:23
LastEditors: CoderXZ
LastEditTime: 2021-05-09 21:46:22
'''
def counter():
    i = 0
    while True:
        i += 1
        yield i
def inc():
    c = counter()
    return next(c)

print(inc())
print(inc())
print(inc())