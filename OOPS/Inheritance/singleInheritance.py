class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Employee name is {self.name} and salary is {self.salary}")


class Programmer(Employee):
    company = "ITC Infotech"

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} Language.")


p = Programmer("John Doe", 50000, "Python")

p.show()
p.showLanguage()
