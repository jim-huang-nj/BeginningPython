'''
Author: your name
Date: 2021-05-22 21:58:50
LastEditTime: 2021-05-22 22:10:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Study\MagePython\Chapter5\5-2-3.py
'''
def add(x,y):
    return x+y

def logger(fn):
    def wrapper(*args,**kwargs):       
        print("begin")
        x = fn(*args,**kwargs)
        print("end")
        return x
    return wrapper

#print(logger(add)(5,y=50))
add = logger(add)
print(add(x=5,y=10))