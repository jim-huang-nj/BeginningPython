'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-08 22:38:41
LastEditors: CoderXZ
LastEditTime: 2021-05-09 21:31:18
'''
def gen():
    print("line 1")
    yield 1
    print("line 2")
    yield 2
    print("line 3")
    return 3
next(gen())
print("="*20)
next(gen())
print("="*20)
g = gen()
print("="*20)
print(next(g))
print(next(g))
print(next(g))
# print(next(g,'End'))