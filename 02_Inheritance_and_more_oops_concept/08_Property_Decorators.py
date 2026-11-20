class Employee:
    def __init__(self):
        self._name = "Akshat"  # Stores the actual name
        self._work = "Developer" #Storing the hard coded work nme
    @property
    def name(self):
        # Getter: Returns the name when we access e.name
        return self._name

    @name.setter
    def name(self, value):
        # Setter: Checks the value before updating the name
        if value != "":
            self._name = value  # Updates if the value is valid
        else:
            print("Invalid name!")  # Rejects an empty value
            
    @property
    def work(self):
        return self._work
    
    @work.setter
    def work(self,value):
        if value != "":
            self._work = value
        else:
            print("Invalid Work Name!")

e = Employee()

print(e.name)      # Calls getter and prints Akshat
e.name = "Rahul"   # Calls setter and updates the name
print(e.name)      # Calls getter and prints Rahul
e.name = ""        # Rejects the empty value
print(e.name)      # Prints Rahul because the old value remains


print(e.work)
e.work = "Frontend Designer"
print(e.work)
e.work = ""
print(e.work)

e.name = input("Enter Your Name : ")
e.work = input("Enter Your Work : ")
print(e.name,"\n",e.work)

# @property:
# Jab hum e.name access karte hain, getter automatically call hota hai
# aur variable ki value return karta hai.

# @name.setter:
# Jab hum e.name = "Rahul" likhte hain, setter automatically call hota hai.
# Setter ke andar hum validation laga sakte hain.
# Agar value valid hai toh variable update hota hai.
# Agar invalid hai toh purani value unchanged rehti hai.

# Main Purpose:
# Property decorator ka use variables ko control karne,
# validation lagane aur direct modification ko manage karne ke liye hota hai.