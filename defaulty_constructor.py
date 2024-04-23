class Employee:
    def __init__(self):
        self.name = "Deki"
        self.age = 20
    def displayEmployee(self):
        x = 'hello' #variable accessible only inside function
        print(x)
        print(f"Name:{self.name} Age:{self.age}")

e1 = Employee()
e1.displayEmployee()