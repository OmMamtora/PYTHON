#Strings are immutable we can't change value of String.
#for example: name = "ABC" i have this string and if i want to change particular character 
#               or string we can't able to change althought it will work on 
#               list we can change value in list

name = "Om Mamtora"

#Finding length of String.
length = len(name)
print(length)

#String Slicing.
slice_Name = name[0:5]
print(slice_Name)

sliceNew = name[0:11]
print(sliceNew)

reverseSlice = name[-4:-1]
print(reverseSlice)

sliceName = name[:6]
print(sliceName)

#Here we are using skip concept and Syntax of this is :- [start : stop: skip]
stringSkip = name[0:7:2] 
print(stringSkip)




#String Function

myString = "Om V Mamtora"

#Find Length of String.
lengthString = len(myString)
print(lengthString)

print("Length of String is ",len(myString))


#This function return value in true or false.
endString = myString.endswith("tora")
print(endString)

endName = myString.endswith("o")
print(endName)

startString = myString.startswith("o")
print(startString)

#TO finding how many rime particular is in string we can use this function.
#It is case sensitive
countChar = myString.count("a")
print(countChar)

print(myString.count("O"))
print(myString.count("m"))

#This function is used to do first letter capital in String.
newString = "hello I am here!!"
print(newString.capitalize())

#This fuction is used for capitalize first character of each word in string.
print(newString.title())


#This function performs uppercase and lowercase of string.
print(newString.lower())
print(newString.upper())

print(name.split(" "))
print(name.split("M"))
print(name.split("m"))