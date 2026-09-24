class Employee:
    def __init__(self, name, language, salary):
        print("I am Creating an object of Employee class")
        self.name = name
        self.language = language
        self.salary = salary
        
    def get_info(self):
        print(f"Name is {self.name}")
        print(f"Language is {self.language}")
        print(f"Salary is {self.salary}")
        
    
    
Akshat = Employee("Akshat", "Python", 15000)
Akshat.get_info()

#def __init__ is a constructor initializer which is called when an object of the class is created.
# It is used to initialize the attributes of the class.
# We doesn,t need to call the __init__ methjod because it gets callld automatically
#when an object of the class is created.
#its known as Dunder methjod because it uses double underscore before and after the method name.