class Employee:
    language = "Python"
    salary = 1500000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

emp = Employee()
emp.name = "Om"

print("Name of employee is",emp.name,"and language is",emp.language,"and salary is",emp.salary)

print()

emp.getInfo()
