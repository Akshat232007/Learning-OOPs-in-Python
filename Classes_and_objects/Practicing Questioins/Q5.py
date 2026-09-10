# write a class Train which has methods to book a ticket , get status (no of seats)
# and get fair infromation of train running under indian railways.


import random


class Train:
    
    def __init__(self, train_no):
        self.train_no = train_no

    def book_ticket(self, Fro, To):
        print(f"Ticket is booked in train number {self.train_no} from {Fro} to {To}S")
    
    def get_status(self):
        print(f"Train number {self.train_no} is on time")
    
    def get_fair(self, Fro, To):
        print(f"Fair information for train number {self.train_no} from {Fro} to {To}: ₹{random.randint(100, 1000)}")
        
p1=Train(12345)
p1.book_ticket("Delhi", "Mumbai")
p1.get_status()
p1.get_fair("Delhi", "Mumbai")
