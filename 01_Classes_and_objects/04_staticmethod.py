class Employee:
    Language = "Python"
    Salary = 15000
    
    def get_info(self):
        print(f"Language is {self.Language}")
        print(f"Salary is {self.Salary}")
        
    @staticmethod
    def greet():
        print("Hello, I am an employee.")
        
Akshat = Employee()
Akshat.get_info()
Akshat.greet()

#we use static method because we don't want to pass the whole object as an argument to the method
#which the methed isn't going to use.
#Static methods are used when we want to define a method that doesn't depend on the instance of the class.