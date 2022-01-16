'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-09 16:26:04
LastEditors: CoderXZ
LastEditTime: 2021-05-09 20:30:36
'''

# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
# g = foo()
# print(next(g))
# print("*"*20)
# print(next(g))


def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num
for n in foo(0):
    print(n)