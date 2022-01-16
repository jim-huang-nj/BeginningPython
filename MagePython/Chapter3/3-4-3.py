'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-03 09:56:35
LastEditors: CoderXZ
LastEditTime: 2021-05-03 10:34:02
练习（要求使用列表解析式完成）
返回1-10平方的列表
有一个列表lst = [1,4,9,16,2,5,10,15]，生成一个新列表，要求新列表元素是lst相邻2项的和打印九九乘法表
"0001.abadicddws" 是ID格式，要求ID格式是以点号分割，左边是4位从1开始的整数，右边是10位随机小写英文字母。请依次生成前100个ID的列表
'''
import random
lst1 = [i**2 for i in range(1,11)]
print(lst1)

lst2 = [1,4,9,16,2,5,10,15]
lst3 = [lst2[i]+lst2[i+1] for i in range(len(lst2)-1)]
print(lst3)

[print("{0:<2}* {1:<2} = {2:<2}  ".format(j,i,i*j), end="\n" if i==j else "") for i in range(1,10) for j in range(1,i+1) ]

idstr = ["{:04}.{}".format(i, "".join([(chr(random.randint(97,122))) for j in range(10)])) for i in range(1,101) ]
print(idstr)

