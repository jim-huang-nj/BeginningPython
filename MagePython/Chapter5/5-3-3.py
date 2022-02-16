def copy_properties(src,dst):
    dst.__name__=src.__name__
    dst.__doc__ = src.__doc__

def logger(fn):
    def wrapper(*args,**kwargs):
        """I am wrapper"""
        print("begin")
        x = fn(*args,**kwargs)
        print("end")
        return x
    copy_properties(fn,wrapper)
    return wrapper

@logger #add = logger(add)
def add(x,y):
    """This is a function for add"""
    return x + y

print(add(4,5))
print("name={},doc={}".format(add.__name__,add.__doc__))