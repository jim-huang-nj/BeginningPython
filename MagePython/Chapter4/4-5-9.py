'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-09 22:23:46
LastEditors: CoderXZ
LastEditTime: 2021-05-09 22:24:51
'''
def inc():
    for x in range(1000):
        yield x

foo = inc()
print(next(foo))
print(next(foo))
print(next(foo))