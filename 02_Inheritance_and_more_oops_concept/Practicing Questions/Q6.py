#write __str__() method to print the Vectors as follows : 7i + 3j + 4k
# Assume the Vector of 3 dimension


class Vector:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, other):
        result = Vector(self._x + other._x,self._y + other._y,self._z + other._z)
        return result

    def __mul__(self, other):
        
        #Here we are not defining an vector obj becuase we only want to display an integer not an vector so __str__ will not be called for this
        
        dot_p = (self._x * other._x + self._y * other._y + self._z * other._z)
        return dot_p

    def __str__(self):
        result = ""

        if self._x != 0:
            result += f"{self._x}i"

        if self._y > 0:
            result += f" + {self._y}j"
        elif self._y < 0:
            result += f" - {abs(self._y)}j"

        if self._z > 0:
            result += f" + {self._z}k"
        elif self._z < 0:
            result += f" - {abs(self._z)}k"

        return result if result else "0"


V1 = Vector(23, 5)
V2 = Vector(43, 54, 9)

print("Sum :", V1 + V2)
print("Dot Product:", V1 * V2)