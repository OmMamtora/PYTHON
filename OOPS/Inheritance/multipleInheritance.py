class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Employee name is {self.name} and salary is {self.salary}")

class coder:
    language = "Python" 
    def printLanguages(self):
        print(f"Out of all the languages your language is {self.language}")
         



class Programmer(Employee,coder):
    company = "ITC Infotech"

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} Language.")


p = Programmer("John Doe", 50000, "Python")

p.show()
p.showLanguage()
p.printLanguages()
