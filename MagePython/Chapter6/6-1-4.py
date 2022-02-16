'''
Author: Jim Huang
Date: 2022-02-16 14:16:04
LastEditors: Jim Huang
LastEditTime: 2022-02-16 14:21:05
Description: 请填写简介
'''
f = open ("test","w+")
lines = ["abc","123\n","magedu"]
f.writelines(lines)

f.seek(0)
print(f.read())
f.close()
