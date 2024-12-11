#Check if a given number is positive, negative, or zero.

num = int(input("Enter Number:->"))

if num < 0:
    print(num,"is negative.")
elif num > 0:
    print(num,"is positive.")
else:
    print("Number is zero.")


# Determine whether a number is even or odd.

n = int(input("Enter Number:->"))

if n %2==0:
    print(n,"is even number.")
else:
    print(n,"is odd number.")


#Decide if a person is eligible to vote based on their age.

age = int(input("Enter age:"))

if age >= 18:
    print("Congratulations! you are eligible for vote..")
else:
    print("Sorry! you are under 18..")


#Given a student's marks, determine their grade using a grading system (e.g., A, B, C, etc.).

name=input("Enter name:->")

total_marks = 0

for i in range(5):
    marks = int(input("Enter marks for subject:-> "))
    total_marks += marks

average_marks = total_marks / 5

if average_marks >= 90:
    grade = 'A'
elif average_marks >= 80:
    grade = 'B'
elif average_marks >= 70:
    grade = 'C'
elif average_marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"\nStudent Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Grade: {grade}")


#Check if a year is a leap year.

year = int(input("Enter year:->"))

if(year % 4==0 and year % 100 !=0) or year % 400 == 0:
    print(f"Year is leap year {year}")
else:
    print(f"Year is not leap year {year}")


#Write a program to determine whether a triangle is equilateral, isosceles, or scalene based on its side lengths.

side1 = float(input("Enter value for side 1:->"))
side2 = float(input("Enter value for side 2:->"))
side3 = float(input("Enter value for side 3::->"))

if(side1 <=0 or side2 <=0 or side3 <=0):
    print("Enter valid value..")
elif(side1 == side2 == side3):
    print("Triangle is equilateral")
elif(side1== side2 or side1==side3 or side2==side3):
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")

#Create a program that classifies a given character as a vowel, consonant, digit, or special character.

char = input("Enter a character:-> ")

if len(char) == 1:
    if char.lower() in 'aeiou':
        print(f"{char} is a vowel.")
    elif char.isalpha():
        print(f"{char} is a consonant.")
    elif char.isdigit(): 
        print(f"{char} is a digit.")
    else:
        print(f"{char} is a special character.")
else:
    print("Please enter only a single character.")


#If you can find lines like this make a lot of money, buy now, click here, visit page report as spam.

lst = ["make a lot of money", "buy now", "click here", "visit page"]

msg = input("Enter comment:->")

if msg in lst:
    print(f"{msg} this is spam message..")
else:
    print(f"{msg} this message is not spam message..")
