class Employee:
    def __init__(self, ID, name, Salary):
        self.ID = ID
        self.name = name
        self.Salary = Salary
        
    def show_details(self):
        print(f"ID : {self.ID}\nName : {self.name}\nSalary : {self.Salary}")
        

class Developer(Employee):
    def __init__(self, ID, name, Salary, Intro):
        super().__init__(ID, name, Salary)
        self.Intro = Intro
        
    def display_details(self):
        print(f"ID : {self.ID}\nName : {self.name}\nSalary : {self.Salary}\nIntro :{self.Intro}")
        
class Manager(Employee):
    def __init__(self, ID, name, Salary, Intro):
        super().__init__(ID, name, Salary)
        self.Intro = Intro
        
    def display_details(self):
        print(f"ID : {self.ID}\nName : {self.name}\nSalary : {self.Salary}\nIntro :{self.Intro}")
    
    
e1 = Developer("23", "Akshat", "232000" ,"Hi am a Python Developer i built working backend using python")
e1.display_details()

e2 = Manager("25", "Tejas", "12000", "Hi am a Team Manaer i manage the team work integration bteween all the team memners working under me")
e2.display_details()