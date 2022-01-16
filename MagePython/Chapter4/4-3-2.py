import datetime
start = datetime.datetime.now()
pre = 0
cur = 1
print(cur,end=" ")
n = 50
for i in range(n-1):
    pre,cur = cur, pre + cur
    print(cur,end=" ")

print()
print("="*30)
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)


