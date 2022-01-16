'''
Author: your name
Date: 2021-05-22 21:53:42
LastEditTime: 2021-05-22 21:55:05
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Study\MagePython\Chapter5\5-2-1.py
'''
def add(x,y):
    return x+y

def logger(fn):
    print("begin")
    x = fn(4,5)
    print("end")
    return x

print(logger(add))