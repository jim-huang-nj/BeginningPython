'''
Author: Jim Huang
Date: 2022-01-25 08:51:03
LastEditors: Jim Huang
LastEditTime: 2022-01-28 16:00:52
Description: 请填写简介
'''

def counter():
    count = 0
    def inc():
        nonlocal count
        #count +=1
        return count
    return inc
foo = counter()
#foo = counter()
foo()