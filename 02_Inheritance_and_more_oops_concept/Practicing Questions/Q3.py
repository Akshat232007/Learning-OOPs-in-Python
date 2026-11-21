#create a class 'Employee' and add salary and increment properties to it.

#Write a method 'salaryafterincrement' method with a @property decorator with a setter which changes  the value of
#increment based on the salary. 

class Employee:
    def __init__(self, name: str, salary: int, increment=0):
        self._name = name
        self._salary = salary
        self._increment = 0
        self.increment = increment

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, increment_value):
        if increment_value >= 0:
            self._increment = increment_value
            self._salary = self._salary * (1 + (increment_value / 100))
            print(f"New Salary becomes: {self._salary}")
        else:
            print("Increment cannot be less than 0")

    @property
    def salary(self):
        return self._salary


E1 = Employee("Akshat", 2000)
E1.increment = 10

E2 = Employee("Raj", 1000, 10)
print(E2.salary)
