'''
Author: Jim Huang
Date: 2022-01-29 17:53:40
LastEditors: Jim Huang
LastEditTime: 2022-01-29 17:55:56
Description: 请填写简介
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

