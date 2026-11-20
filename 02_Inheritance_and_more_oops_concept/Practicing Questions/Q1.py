#Create a class 2d Vector and use it to create another class representing a 3d vector.


class TwoDVector:
    def __init__(self, i,j):
        self.i = i
        self.j = j
    
    def display(self):
        print(f"{self.i}i + {self.j}j")

class ThreeDvector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
        
    def display(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")
        
        
twoD = TwoDVector(23,5)
twoD.display()

threeD = ThreeDvector(223,54,2)
threeD.super().display()
