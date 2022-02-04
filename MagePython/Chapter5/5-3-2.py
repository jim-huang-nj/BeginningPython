from tkinter import Y


def logger(fn):
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

print("name={},doc={}".format(add.__name__,add.__doc__))