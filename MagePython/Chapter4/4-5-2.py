'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-08 22:38:41
LastEditors: Jim Huang
LastEditTime: 2022-01-29 16:44:54
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
print("*"*20)
#print(next(g))
print(next(g,'End'))
#print(next(g))