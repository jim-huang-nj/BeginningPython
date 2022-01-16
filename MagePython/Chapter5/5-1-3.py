'''
Author: your name
Date: 2021-05-22 14:57:47
LastEditTime: 2021-05-22 14:59:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Study\MagePython\Chapter5\5-1-3.py
'''
def sort(iterable,key = lambda a,b : a >b):
    ret = []
    for x in iterable:
        for i,y in enumerate(ret):
            if key(x,y):
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret

print(sort([1,2,3,4,5,6]))
print(sort([6, 5, 4, 3, 2, 1]))