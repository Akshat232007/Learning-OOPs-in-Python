#Create a class with a class attribute a; create an object from it and set a
#directly using object .a = 0.Does this change the clss attribute

class demo:
    a = 10
    
    
obj = demo()
obj.a = 0
print(f"Object attribute a: {obj.a}")

print(f"Class attribute a: {demo.a}")

#Here we are calling the class attribute using the class name and it will print 10 because 
# we have not changed the class attribute.
# We have only created an instance attribute with the same name as the class attribute.