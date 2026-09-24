class Employee:
    Language = "Python"
    Salary = 15000
    
    def get_info(self):
        print(f"Language is {self.Language}")
        print(f"Salary is {self.Salary}")
    
Akshat = Employee()

Akshat.get_info()
#can also be called as Employee.get_info(Akshat)

# the error "Employee.get_info() takes 0 positional arguments but 1 was given" 
# occurs because when you call a method/function of a class it gets converted into 
# Employee.get_info(Akshat) and hence the error came because in converted form we are
# passing the object as an argument. To avoid this we use self as 
# the first parameter of the method/function.