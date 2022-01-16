# -*- coding: utf-8 -*-
# @Time  : 2020/11/18 18:53
# @Author : Jim Huang！！
# @FileName: 1-5.py
# @Software: PyCharm
# 打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+" * "+str(i)+" = "+str(i*j)+"\t",end='')
    print()
# 打印九九乘法表
print()

for i in range(1,10):
    for j in range(i,10):
        print(str(i) + " * " + str(j) + " = " + str(i * j) + "\t", end='')
    print()
    for c in range(1,i+1):
        print(" "*9+"\t",end="")

# 打印九九乘法表
print()
for i in range(1,10):
    line=""
    for j in range(1,i+1):
        line+="{0} * {1} = {2}\t".format(j,i,i*j)
    print(line)

