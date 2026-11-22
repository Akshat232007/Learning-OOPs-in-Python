#write a class complex to represent complex numbers , along with overloaded operators '+' and "*" 
# which add and multilpies them.

class Complex:
    def __init__(self, a : int, b : int) -> None:
        self._a = a
        self._b = b
        
    def  __add__(self, other) -> Complex:
        return Complex((self._a + other._a), (self._b + other._b))
    
    def __mul__(self, other) -> Complex:
        self.r = (self._a * other._a) - (self._b * other._b)
        self.i = (self._a * other._b) + (self._b * other._a)
        return Complex(self.r, self.i) # same here also
    
    def __str__(self) -> str:
        return f"{self._a} + {self._b}i"
        
C1 = Complex(23,5)
C2 = Complex(89,8)


print(C1 + C2)
print(C1 * C2)



# We use our own Complex class to store the calculated values.
# __str__() accesses those values and displays them in a readable format.

# __add__() creates a new Complex object using the calculated
# real and imaginary values instead of modifying the original objects.
# The new object stores these values in its own _a and _b attributes.

# __mul__() does the same after calculating the multiplication result.

# __str__() accesses the values stored in the current Complex object
# and converts them into a readable string for display.