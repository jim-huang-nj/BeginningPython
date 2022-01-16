def foo(w,u='abc',*,z=123,zz=[456]):
    u = 'xyz'
    z = 789
    zz.append(1)
    print(w,u,z,zz)

print(foo.__defaults__)
foo('magedu')
print(foo.__kwdefaults__)
