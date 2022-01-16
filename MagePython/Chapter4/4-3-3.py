import sys
import datetime
start = datetime.datetime.now()
def fib(n):
    return 1 if n < 2 else fib(n-1) + fib(n-2)

for i in range(30):
    print(fib(i),end =" ")

#print(sys.getrecursionlimit())
print()
print("="*30)
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)