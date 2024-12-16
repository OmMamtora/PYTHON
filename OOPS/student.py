class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def disply(self):
        print(f"Student name is {self.name} and marks is {self.marks}",end = ".")
    
std = Student("Om","94")

std.disply()
        