class Employee:
    a = 1

class coder(Employee):
   b = 2

class Programmer(coder):
    c = 3


# e = Employee()
# print(e.a)

# c = coder()
# print(c.a,c.b) #output : 1 2
# print(c.b) #output : 1

p = Programmer()
print(p.a,p.b,p.c) #output : 1 2 3
print(p.c) #output : 3