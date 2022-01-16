'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-04 20:49:03
LastEditors: CoderXZ
LastEditTime: 2021-05-04 22:44:08
'''
def makepicture(x):
    for i in range(1,x+1):
        for j in range(x,0,-1):
            if j <= i:
                print("{:>4}".format(j),end="")
            else:
                print("    ",end="")
        print("") 
    for i in range(x,0,-1):
        if i != x:
            print("    "*(x-i),end="")
        for j in range(i,0,-1):
            print("{:>4}".format(j),end="")
        print()

makepicture(12)