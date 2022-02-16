import  datetime,time,functools


def logger(duration,func=lambda name,duration:print("{} took {}s".format(name,duration))):
    def _logger(fn):
        @functools.wraps(fn)
        def wrapper(*args,**kwargs):
            """I am wrapper"""
            start = datetime.datetime.now()
            ret = fn(*args,**kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            if delta > duration:
                func(fn.__name__, duration)
            return ret
        return wrapper
    return _logger

@logger(5) #add = logger(add)
def add(x,y):
    """This is a function for add"""
    time.sleep(1)
    return x + y

print(add(5,6),add.__name__,add.__wrapped__,add.__dict__,sep="\n")
#print("name={},doc={}".format(add.__name__,add.__doc__))