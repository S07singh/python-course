class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Pyhton"
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")




class Programmer(Employee, Coder):
    salary = 120000
    def showLanguage(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()