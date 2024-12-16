class Rectangle_calculate:

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


length = float(input("Enter length of rectangle:->"))
width = float(input("Enter length of width:->"))

cal = Rectangle_calculate(length , width)

print(f"Area of rectangle is {cal.area()}.")
print(f"Perimeter of rectangle is {cal.perimeter()}.")