'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-09 21:49:17
LastEditors: CoderXZ
LastEditTime: 2021-05-09 21:55:03
'''
def inc():
    def counter():
        print("Hello, this is generater")
        i = 0
        while True:
            i += 1
            yield i
    c = counter()
    return lambda  : next(c)
foo = inc()
print("="*20)
print(foo())
print(foo())