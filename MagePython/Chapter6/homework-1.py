'''
Author: Jim Huang
Date: 2022-02-16 14:48:18
LastEditors: Jim Huang
LastEditTime: 2022-02-16 14:59:31
Description: file copy
'''
filename1 = "test1.txt"
filename2 = "test2.txt"

f = open(filename1,"w+")
lines = ["abc","123","magedu"]
f.writelines("\n".join(lines))
#f.writelines(lines)
f.seek(0)
print(f.read())
f.close()

def copy(src,des):
    with open(src) as f1:
        with open(des,"w") as f2:
            f2.write(f1.read())

copy(filename1,filename2)