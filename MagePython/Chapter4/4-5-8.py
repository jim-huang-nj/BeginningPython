'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-09 22:13:46
LastEditors: CoderXZ
LastEditTime: 2021-05-09 22:16:23
'''
def fib():
    x = 0 
    y = 1
    while True:
        yield y
        x,y = y, x+y
foo = fib()
for _ in range(5):
    print(next(foo))
    
for _ in range(100):
    next(foo)
print(next(foo))