def fib(n,pre=0,cur=1):
    pre,cur = cur,pre + cur
    if n == 0:
        return pre
    return fib(n-1,pre,cur)

print(fib(6))