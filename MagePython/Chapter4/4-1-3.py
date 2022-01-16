'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-04 22:47:55
LastEditors: CoderXZ
LastEditTime: 2021-05-04 22:58:16
'''
def makepicture(x):
    for i in range(1,x+1):
        for j in range(x,0,-1):
            if j <= i:
                print("{:>4}".format(j),end="")
            else:
                print("    ",end="")
        
        print(" "*4,end="")
        flag = True
        for k in range(x-i+1,0,-1):
            if (k < x) & flag:
                print("    "*(x-k),end="")
            flag = False
            print("{:>4}".format(k),end="")
        print()


makepicture(12)