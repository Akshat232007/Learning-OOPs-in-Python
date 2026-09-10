class Employee:
    Language = "Python"
    Salary = 15000
    
Akshat = Employee()
Akshat.name = "Akshat"

Akshat.Language = "Javascript"
print( Akshat.name , Akshat.Language , Akshat.Salary)

# Here we can see that the instance/object attributes are higher in preference than class attributes