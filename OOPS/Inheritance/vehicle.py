# Define a Vehicle class with attributes like brand and year. Create a subclass Car that 
# adds an attribute fuel_type and a method to display all details.

class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year,fuel_type):
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    def display(self):
        print(f"Car brand name is {self.brand}, year is {self.year} and fule type is {self.fuel_type}")


c = Car("Mercedes",2024,"Diesel")
c.display()