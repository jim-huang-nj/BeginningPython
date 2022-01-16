'''
Author: your name
Date: 2021-05-22 21:56:15
LastEditTime: 2021-05-22 21:57:28
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Study\MagePython\Chapter5\5-2-2.py
'''
def add(x,y):
    return x+y

def logger(fn, *args, **kwargs):
    print("begin")
    x = fn(*args,**kwargs)
    print("end")
    return x

print(logger(add,5,y=60))