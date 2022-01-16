# 

def f(n):
    return 1 if n==1 else n*f(n-1)

print(f(4))

lst = list()
data = str(1234)
def revert(x):
    if x == -1:
        return []
    return [data[x]] + revert(x-1)
print(revert(len(data)-1))

def peach(days=10):
    if days == 1:
        return 1
    return (peach(days+1)+1)*2
print(peach())