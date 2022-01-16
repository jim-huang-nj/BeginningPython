from collections import namedtuple
import random
Student = namedtuple("Student","name age")
tom = Student("tom",20)
jerry = Student("jerry",18)
print(tom[1])
print(jerry)


Student = namedtuple('Student', ['name', 'age', 'DOB'])
 
# Adding values
S = Student('Nandini', '19', '2541997')
 
# Access using index
print("The Student age using index is : ", end="")
print(S[1])
 
# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

lst = []
for x in range(10):
    lst.append(random.randint(1,600))
print(lst)
print("Max 的数：",max(lst))    
lst.sort()
print(lst)