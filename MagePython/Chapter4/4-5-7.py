'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-09 21:49:17
LastEditors: Jim Huang
LastEditTime: 2022-01-29 17:46:48
'''
def inc():
    def counter():
        print("Hello, this is generater")
        i = 0
        while True:
            i += 1
            #yield i
    c = counter()
    return lambda  : next(c)



    
print(id(inc))    
foo = inc()
print(id(foo))
print("="*20)
print(foo())
print(foo())