def copy_properties(src):
    def _copy(dst):
        dst.__name__=src.__name__
        dst.__doc__ = src.__doc__
        return dst
    return _copy

def logger(fn):
    @copy_properties(fn) #wrapper = copy_propertiest(fn)(wrapper)
    def wrapper(*args,**kwargs):
        """I am wrapper"""
        print("begin")
        x = fn(*args,**kwargs)
        print("end")
        return x
    return wrapper

@logger #add = logger(add)
def add(x,y):
    """This is a function for add"""
    return x + y

print(add(4,5))
print("name={},doc={}".format(add.__name__,add.__doc__))