# Create a Person class with attributes like name and age, and a method to display details. 
# Inherit it in a Student class that adds an attribute grade and overrides the method to 
# include grade details.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name is {self.name} and age is {self.age}")


class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade

    def studentShow(self):
        print(f"Name of student is {self.name}, age is {self.age} and grade is {self.grade}")


s = Student("Om",20,"A++")
s.studentShow()