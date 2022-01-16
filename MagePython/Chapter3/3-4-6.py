'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-03 13:51:07
LastEditors: CoderXZ
LastEditTime: 2021-05-03 13:59:46
'''
for x in iter(range(10)):
    print(x)

g = (x for x in range(10))
print(type(g))
print(next(g))
print(next(g))

a = list(zip(range(10),range(10)))
b = list(zip(range(10),range(10),range(5),range(10)))
print(a)
print("="*10)
print(b)

d = dict(zip(range(10),range(10)))
print(d)