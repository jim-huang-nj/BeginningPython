'''
Author: Jim Huang
Date: 2022-02-16 10:57:54
LastEditors: Jim Huang
LastEditTime: 2022-02-16 11:01:03
Description: 请填写简介
'''
f = open("test","w")
f.write("python\rwww.python.org\nwww.magedu.com\r\npython3")
f.close()

newlines = [None, "","\n","\r\n"]
for nl in newlines:
    f = open("test","r+",newline=nl)
    print(f.readlines())
    f.close()