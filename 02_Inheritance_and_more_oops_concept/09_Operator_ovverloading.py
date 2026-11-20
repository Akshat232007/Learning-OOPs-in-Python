class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self, other):
        return self.value - other.value

a = Number(20)
b = Number(89)

print(a + b)
print(a - b)


# Python is built around objects and classes.
# Whenever we use an operator like + or - with our custom class objects,
# Python calls a special method automatically.

# For example:
# a + b calls a.__add__(b).
# a - b calls a.__sub__(b).

# Here, a becomes self and b becomes other.
# Inside these methods, we define what the operators should do with our objects.
# In simple words: Operator overloading means giving existing operators like +, -, * and /
# the ability to perform operations on objects of our own class by defining special methods.

# Operator overloading allows us to define how operators like +, -, * and / work with objects of our own class.

# 1. First, we create a class named Number and define the __add__() and __sub__() methods inside it.
# 2. We create two objects, a and b, with values 20 and 89.
# 3. When we write a + b, Python checks the class of object a and looks for the __add__() method.
# 4. Since __add__() is defined inside the Number class, Python automatically calls it as a.__add__(b).
# 5. Inside the method, self refers to object a and other refers to object b.
# 6. Using self.value + other.value, Python accesses the values stored in both objects, adds them and returns the result 109.
# 7. Similarly, when we write a - b, Python calls a.__sub__(b) and performs subtraction using the values stored in both objects, returning -69.