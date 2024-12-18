# Design a Device class with attributes like brand and model. Create subclasses Phone and 
# Laptop that add specific attributes and methods (e.g., make_call() for Phone and 
# compile_code() for Laptop).

class Device:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand name is {self.brand} and model number is {self.model}")

class Phone(Device):
    def __init__(self, brand, model,phone_no):
        super().__init__(brand, model)
        self.phone_no = phone_no
    
    def make_call(self, number):
        print(f"Calling {number} from {self.phone_no}")
        

class Laptop(Device):
    def __init__(self, brand, model, processor):
        super().__init__(brand,model)
        self.processor = processor

    def compile_code(self):
        print(f"Compiling code on the {self.processor} processor.")

phone = Phone("Apple", "iPhone 14", "9874563210")
phone.display()  
phone.make_call("987-654-3210")
print("\n")
laptop = Laptop("HP", "Victus", "Intel i7")
laptop.display() 
laptop.compile_code() 