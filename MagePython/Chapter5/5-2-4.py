'''
Author: your name
Date: 2021-05-22 22:16:46
LastEditTime: 2021-05-22 22:40:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Study\MagePython\Chapter5\5-2-4.py
'''


def logger(fn):
    def wrapper(*args,**kwargs):       
        print("begin")
        x = fn(*args,**kwargs)
        print("end")
        return x
    return wrapper

@logger
def add(x,y):
    return x+y

print(add(45,40))