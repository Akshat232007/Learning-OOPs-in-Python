#Create a class "Pets" from a class "Animals" and further create a classs "Dog" from "Pets".
#Add a method "bark" to class "Dog".

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    
    @staticmethod
    def bark():
        print("Bark Bark!")
        
D = Dog()
D.bark()


# @staticmethod was necessary because when we will call the bark function it needs one argumment, but we dont want to 
# pass anything thats the reason