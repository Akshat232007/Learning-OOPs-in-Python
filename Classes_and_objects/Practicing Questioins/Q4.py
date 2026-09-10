# Add a static method in Q2, to greet the user with hello.

# Write a class Calculator capable of finding square , cube and squeare root of a number.

class Calculator:
    def __init__(self, number):
        self.number = number
    
    @staticmethod    
    def greet_user():
        return "Hello, welcome to the Calculator!"
        
    def square(self):
        return f"The square of {self.number} is {self.number ** 2}"
    
    def cube(self):
        return f"The cube of {self.number} is {self.number ** 3}"
    
    def square_root(self):
        return f"The square root of {self.number} is {self.number ** 0.5}"
    
a = Calculator(4)
print(a.greet_user())
print(a.square())
print(a.cube())
print(a.square_root())