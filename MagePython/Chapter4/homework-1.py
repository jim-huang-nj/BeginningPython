'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-09 22:30:47
LastEditors: CoderXZ
LastEditTime: 2021-05-15 21:56:59
'''
source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
target = {}

def flatmap(src, prefix = ""):
    for k,v in src.items():
        if isinstance(v,(tuple,list,dict)):
            flatmap(v,prefix=prefix+k+".")
        else:
            target[prefix+k] = v
    return target
flatmap(source)
print(target)

