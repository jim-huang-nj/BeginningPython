'''
Author: your name
Date: 2021-05-22 15:22:12
LastEditTime: 2021-05-22 15:23:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Study\MagePython\Chapter5\5-1-6.py
'''
def add(x):
    def _add(y):
        return x+y
    return _add

print(add(5)(6))