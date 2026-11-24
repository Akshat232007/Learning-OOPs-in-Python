
# Write a class Vector to represent a 3-dimensional vector.
# Overload + and * operators to calculate sum and dot product.


# This Approach is only limited till 3d.
class Vector:
    def __init__(self, *Coordinates):
        self._Coordinates = Coordinates

    def __add__(self, other):
        result = Vector(*[
            self._Coordinates[i] + (other._Coordinates[i] if i < len(other._Coordinates) else 0)
            for i in range(len(self._Coordinates))
        ])

        return result

    def __mul__(self, other):

        # Here we are not defining a vector obj because we only want to display an integer, not a vector, so __str__ will not be called for this

        result = sum(
            self._Coordinates[i] * other._Coordinates[i]
            for i in range(min(len(self), len(other)))
        )

        return result


    def __str__(self):
        result = ""

        for i in range(len(self)):
            if self._Coordinates[i] == 0:
                continue

            variable = chr(105 + i)

            if result == "":
                result += f"{self._Coordinates[i]}{variable}"
            elif self._Coordinates[i] > 0:
                result += f" + {self._Coordinates[i]}{variable}"
            else:
                result += f" - {abs(self._Coordinates[i])}{variable}"

        return result if result else "0"


V1 = Vector(23, 5, 8, 10)
V2 = Vector(43, 54, 9)

print("V1:", V1)
print("V2:", V2)

print("Sum:", V1 + V2)
print("Dot Product:", V1 * V2)

