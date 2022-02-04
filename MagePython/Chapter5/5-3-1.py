def add(x,y):
    """This is a function of addition"""
    a = x + y
    return x + y

print("name={}\ndoc={}".format(add.__name__,add.__doc__))
print(help(add))    