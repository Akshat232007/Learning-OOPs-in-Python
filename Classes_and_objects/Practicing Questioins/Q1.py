#Create a class Programmer for storing information of few programmers working 
#at microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, PIN):
        self.name = name
        self.salary = salary
        self.PIN = PIN
    def info(self):
        print(f"The name of the programmer is {self.name}")
        print(f"The salary of the programmer is {self.salary}")
        print(f"The PIN of the programmer is {self.PIN}")
        
E1 = Programmer("Akshat", 15000, 1234)
E2 = Programmer("Rohit", 20000, 5678)

E1.info()
E2.info()