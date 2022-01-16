'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-08 21:49:16
LastEditors: CoderXZ
LastEditTime: 2021-05-08 22:37:35
'''
def inc():
    for i in range(5):
        yield i
print(type(inc))
print("="*10)
print(type(inc()))
x = inc()
print(type(x))
print(next(x))
for m in x:
    print(m,'*')
for m in x:
    print(m,'**')
    
    
print("="*30)
y = (i for i in range(5))
print(type(y))
print(next(y))
print(next(y))