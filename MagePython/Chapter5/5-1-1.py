def counter(base):
    def inc(step=1):
        nonlocal base
        base +=step
        return base
    return inc
f1 = counter(10)
print(f1())
f2 = counter(10)
print(f2())
print(f1==f2)