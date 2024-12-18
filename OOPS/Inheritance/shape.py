# Write a Shape class with a method area() that returns 0. Create a subclass Rectangle 
# with attributes length and width, and override the area() method to calculate the 
# rectangle's area.

class Shape:
    def area():
        return 0
    

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


l = float(input("Enter Length:->"))
w = float(input("Enter width:->"))

r = Rectangle(l,w)

print(f"Area of rectangle is {r.area()}")