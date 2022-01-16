'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-05-01 14:55:57
LastEditors: CoderXZ
LastEditTime: 2021-05-01 15:06:05
用户输入一个数字判断是几位数打印每一位数字及其重复的次数依次打印每一位数字，顺序个、十、百、千、万...位
输入5个数字，打印每个数字的位数，将这些数字排序打印，要求升序打印
'''
randnumber = int(input("Please input one number:"))
rand_str = str(randnumber)
print("Total number bit is {0} ".format(len(rand_str)))
for i in range(len(rand_str)):
    print(rand_str[-1-i])