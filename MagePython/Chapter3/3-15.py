'''
Descripttion: 
version: 
Author: Jim Huang
Date: 2021-02-19 21:32:13
LastEditors: CoderXZ
LastEditTime: 2021-05-03 15:17:55
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Jim Huang
@contact:Jim_Huang@trendmicr.com
@version: 1.0.0
@license: Apache Licence
@file: 3-15.py
@time: 2020/12/9 10:24
排序
"""
nums =  [ 1,9,8,5,6,7,4,3,2]
lenght = len(nums)
print(nums)
count_swap = 0
count_iter = 0

for i in range(lenght):
    maxindex = i
    for j in range(i+1, lenght):
        count_iter +=1
        if nums[maxindex] < nums[j]:
            nums[maxindex],nums[j] = nums[j],nums[maxindex]
            count_swap +=1
print( nums)
print("counter_iter is {0}, count_swap is {1}".format( count_iter,count_swap))

#双向最大最小同时进行 ,注意大的比过了，有可能被小的换掉，恰好不比了导致错误
#nums =  [ 1,2,3,4,5,6,7,8,9]
#nums =  [ 9,8,7,6,5,4,3,2,1]
#nums = [1,9,8,5,6,7,4,3,2]
nums = [1,1,1,1,1,1,1,1,1]
count_swap = 0
count_iter = 0


for i in range(lenght//2):
    #print(nums)
    maxindex = i
    minindex = -1-i
    for j in range(i+1,lenght):
        count_iter+=1
        if nums[maxindex] < nums[j]:
            nums[maxindex],nums[j] = nums[j],nums[maxindex]
            count_swap +=1
        if nums[minindex] > nums[-1-j]:
            nums[minindex],nums[-1-j] = nums[-1-j],nums[minindex]
            count_swap +=1
#只有奇数会有这个问题，再比较一下，小的不会出错
if nums[i] < nums[i+1]:
    nums[i],nums[i+1] = nums[i+1],nums[i]
    count_swap +=1
print(nums)
print("counter_iter is {0}, count_swap is {1}".format( count_iter,count_swap) )
            