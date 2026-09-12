class Employee:

    def __init__(self, name):
        self.name = name
        print("Employee constructor called")


class Developer(Employee):

    def __init__(self, name, language):
        super().__init__(name)      #we use super().__init() to call the constructor of base class through derived class
        self.language = language
        print("Developer constructor called")


developer = Developer("Akshat", "Python")

print(developer.name)
print(developer.language)