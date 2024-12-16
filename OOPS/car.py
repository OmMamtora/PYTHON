class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Car make is {self.make}.\nModel is {self.model}.\nYear of manufacture is {self.year}")
    
newCar = Car("Maybach", "GLS 300d", 2019)

newCar.display()
