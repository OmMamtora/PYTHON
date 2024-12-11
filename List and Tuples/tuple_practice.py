#Tuple is also immutable so we can not change value in tuple.

my_tuple = (1, 2, 3, "apple", "banana")
print("Original Tuple:", my_tuple)

my_tuple = (1, 2, 3, "apple", "banana")
print("Sliced Tuple (2nd to 4th element):", my_tuple[1:4])

#Concate two tuple
tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana")
result_tuple = tuple1 + tuple2
print("Concatenated Tuple:", result_tuple)

#Here list is convert into tuple.
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print("Converted List to Tuple:", my_tuple)


#ere we are creating nesated tuple and calling value from tuple.
nested_tuple = (1, 2, (3, 4), (5, 6))
print("Nested Tuple:", nested_tuple)
print("Accessing nested tuple element:", nested_tuple[2][1])


#Metods of tuple.

#Check length of tuple.
my_tuple = (1, 2, 3, "apple", "banana")
print("Length of Tuple:", len(my_tuple))

#Here we are checking that value store on which index number.
my_tuple = (1, 2, 3, "apple", "banana")
print("Index of 'apple':", my_tuple.index("apple"))

#Here counting occurance of particular value in tuple.
my_tuple = (1, 2, 3, 2, 2, "apple", "banana")
print("Number of times '2' occurs:", my_tuple.count(2))