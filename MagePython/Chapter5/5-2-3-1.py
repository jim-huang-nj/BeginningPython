def add(x,y):
    return (x+y)

def logger(fn):
    def wrapper(*args,**kwargs):
        x = fn(*args,**kwargs)
        return x
    return wrapper

print(logger(add)(5,y=6))
