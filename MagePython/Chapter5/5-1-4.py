'''
Author: your name
Date: 2021-05-22 15:00:19
LastEditTime: 2021-05-22 15:03:53
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Study\MagePython\Chapter5\5-1-4.py
'''
def sort(iterable,reverse = False, key = lambda a,b : a >b):
    ret = []
    for x in iterable:
        for i,y in enumerate(ret):
            flag = key(x,y) if not reverse else not key(x,y)
            if flag:
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret

print(sort([1,2,3,4,5,6]))
print(sort([6, 5, 4, 3, 2, 1]))