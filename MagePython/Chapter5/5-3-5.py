
import  datetime


def copy_properties(src):
    def _copy(dst):
        dst.__name__=src.__name__
        dst.__doc__ = src.__doc__
        return dst
    return _copy

def logger(duration):
    def _logger(fn):
        @copy_properties(fn) #wrapper = copy_propertiest(fn)(wrapper)
        def wrapper(*args,**kwargs):
            """I am wrapper"""
            start = datetime.datetime.now()
            ret = fn(*args,**kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            print("so slow") if delta > duration else print("so fast")
            return ret
        return wrapper
    return _logger

@logger(5) #add = logger(add)
def add(x,y):
    """This is a function for add"""
    return x + y

print(add(5,6))
print("name={},doc={}".format(add.__name__,add.__doc__))