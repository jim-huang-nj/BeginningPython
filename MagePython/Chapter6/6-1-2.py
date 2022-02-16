'''
Author: Jim Huang
Date: 2022-02-16 11:08:31
LastEditors: Jim Huang
LastEditTime: 2022-02-16 12:04:55
Description: 请填写简介
'''
f = open("test4","r+")
f.write("magedu")
f.write("\n")
f.write("马哥教育")
f.seek(0)
print(f.read(7))
f.close()
f = open("test4","rb+")
print(f.read(7))
print(f.read(1))
f.close()