'''
Author: your name
Date: 2021-05-23 11:03:59
LastEditTime: 2021-05-23 11:15:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Study\MagePython\Chapter5\5-2-5.py
'''
import datetime
import time

def logger(fn):
    def wrap(*args,**kwargs):
        # before enhance function 
        print("arg={},kwarge={}".format(args,kwargs))
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        #after enhance function
        delta= datetime.datetime.now()-start
        print("function {} took {}s.".format(fn.__name__,delta.total_seconds()))
        return ret
    return wrap

@logger
def add(x,y):
    print("===call add =========================")
    time.sleep(6)
    return x + y

print(add(4,y=7))
        