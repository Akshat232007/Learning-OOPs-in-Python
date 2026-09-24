class Employee:
    Language = "Python" #this ia a class attribute
    Salary = 15000
    
Akshat = Employee()
print( Akshat.Language , Akshat.Salary)

rohan = Employee()
rohan.name = "Rohan"  #This is an object/instance attribute
print(rohan.name , rohan.Language , rohan.Salary)

# Here name is object/instance attribute and salary and Language are class attributes as they 
# directly belong to the class