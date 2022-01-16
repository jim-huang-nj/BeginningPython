s1 = "string"
s2 = "string2"
s3 = '''this is a "String" '''
s4 =  "hello \n magedu.com"
s5 = r'hello \n magedu.com'
s6 = "c:\windows\nt"
s7 =  R"c:\windows\nt"
s8 = "c:\windows\\nt"
sql = """select * from user where name='tom'"""
print(s1+"\n"+s2+"\n"+s3+"\n"+s4+"\n"+s5+"\n"+s6+"\n"+s7+"\n"+s8+"\n"+sql)

for c in sql:
    print(c)
    print(type(c))