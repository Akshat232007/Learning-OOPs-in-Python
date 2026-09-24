class Employee:

    def __init__(self, name):
        self.name = name
        print("Employee constructor called")


class Developer(Employee):

    def __init__(self, name, language):
        super().__init__(name)      #we use super().__init() to call the constructor of base class through derived class and we are passing the name to initialize it because it needs that
        self.language = language
        print("Developer constructor called")


developer = Developer("Akshat", "Python")

print(developer.name)
print(developer.language)

# print(Employee.name) 
# `super().__init__(name)` passes `name` to the parent, which sets `self.name` for the object. So `developer.name` works, but `Employee.name` doesn't.