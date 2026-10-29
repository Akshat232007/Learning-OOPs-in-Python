class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        
# class Programmer(Employee):
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
        
#     def showLanguages(self):
#         print(f"The name is {self.name} and he is Good with {self.language} Language")

#         Rather than rwewriting te whole code we will use inheritance , where child class Programmer will
#         inherit the base class and its methods

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is Good with {self.language} Language")
        
        #Here show(self) is function is inherited from base class employee
    
    
a = Employee()
b = Programmer()

print(a.company, b.company)