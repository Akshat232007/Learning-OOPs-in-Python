class Employee:
    def __init__(self, ID, name, Salary):
        self.ID = ID
        self.name = name
        self.Salary = Salary

    def show_details(self):
        print(f"ID : {self.ID}")
        print(f"Name : {self.name}")
        print(f"Salary : {self.Salary}")


class Developer(Employee):
    def __init__(self, ID, name, Salary, language):
        super().__init__(ID, name, Salary)
        self.language = language

    def developer_details(self):
        print(f"Language : {self.language}")


class Manager(Employee):
    def __init__(self, ID, name, Salary, team):
        super().__init__(ID, name, Salary)
        self.team = team

    def manager_details(self):
        print(f"Team : {self.team}")


class TeamLead(Developer, Manager):
    def __init__(self, ID, name, Salary, language, team):
        Employee.__init__(self, ID, name, Salary)
        self.language = language
        self.team = team

    def display_details(self):
        print(f"ID : {self.ID}")
        print(f"Name : {self.name}")
        print(f"Salary : {self.Salary}")
        print(f"Language : {self.language}")
        print(f"Team : {self.team}")


e1 = TeamLead(
    23,
    "Akshat",
    232000,
    "Python",
    "Backend Team"
)

e1.display_details()