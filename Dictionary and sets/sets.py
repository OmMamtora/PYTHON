a = {25,29,45}

#Creating empty set.
empty_set = set()

a.add("Om")
print(a)

#Methods of set.

print("Length of set is ",len(a))

a.remove("Om")
print("After removing value ",a)


b={10,15,20,25}

print(a.union(b))
print(a.intersection(b))

#Practice

#Create set and enter 8 number and display unique value.
s = set()
for i in range(8):
    n = int(input("Enter number:"))
    s.add(n)
print(s)