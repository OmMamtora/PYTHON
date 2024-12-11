#Lists are mutable, we can change value in list.
#It is collection of different type of value.

fruits = ["Apple","Om","Mango","Banana",29,25.25,"Kiwi",True,False]


print(fruits)
print(fruits[7])

#Here i am changing value on index 1
fruits[1] = "Orange"

#Here we can see changes on index 1 and old value replace with new value.
print(fruits[1])

print(fruits[1:4])

#Methods of list

#Sort : It sort a data in ascending order.
nums = [1,5,9,6,22,5,29,25,63,88,52,3,36,7,1]
nums.sort()
print(nums)

#Append:It insert value in list.
fruits.append("Strawberry")
print(fruits)


#Insert : It insert value on particular index.
fruits.insert(3,"Guava")
print(fruits)

#Remove : It removes value from index and if value is not exist in list it gives error.
fruits.remove("Kiwi")
print(fruits)

#Reverse : It retunes list
fruits.reverse()
print(fruits)