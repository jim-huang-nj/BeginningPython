'''
Author: your name
Date: 2021-05-22 14:39:40
LastEditTime: 2021-05-22 14:50:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Study\MagePython\Chapter5\5-1.py
'''
def sort(iterable,reverse = False):
    ret = []
    for x in iterable:
        for i,y in enumerate(ret):
            flag = x > y if reverse else x < y
            if flag:
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret

print(sort([1,2,3,4,5,6]))
             