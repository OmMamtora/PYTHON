# #Basic List Programs

#Python program to interchange first and last elements in a list
nums=[2,8,5,7,12,65,23]
nums[0],nums[-1] = nums[-1],nums[0]
print(nums)


#Python program to swap two elements on index 2,5
nums[2],nums[5] = nums[5],nums[2]
print(nums)


#Ways to find length of list
print("Lengt of String is ",nums.__len__())


#min and max two numbers in Python
min=0
max = 0
for i in nums:
    if i < min:
        min = i
    else:
        max= i
print("Min value is ",min)
print("Max value is ",max)
    

#Maximum of two numbers in Python
a=5
b=15

if a<b:
    print(b)
else:
    print(a)
#     Minimum of two numbers in Python
#Python Ways to check if element exists in list
finder = input("Enter number that you want to find from list:->")
finder = int(finder)

if finder in nums:
    print("Value ",finder," is availble in list")
else:
    print("Opps! Sorry Try again leter")

#Create list and add 5 value on it enter by user.

lst = []

for i in range(5):
    fruit = input(f"Enter Fruit Name {i}:->")
    lst.append(fruit)
print(lst)

#Create list and add 5 student marks and arrange in sorted manner.

marks = []

for i in range(5):
    value = input(f"Enter marks of student :->")
    marks.append(value)
marks.sort()
print(marks)

#sum of 4 numer in list

value = [56,54,6,4]
sum = 0
for i in value:
    sum+= i
print("Sum of list is : ",sum)

