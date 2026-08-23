import random


class Rail:
    def __init__(self,trainNo):
        self.trainNo = trainNo
    def book(self,From,To):
        self.From = From
        self.To = To
        print(f"Ticket is booked on train no:{self.trainNo} from {self.From} to {self.To}")
    
    def getFare(self,From,To):
        self.From = From
        self.To = To
        print(f"Ticket Fare of train no: {self.trainNo} from {From} to {To} is {random.randint(100,999)}")

    def getStatus(self,):
        print(f"Status of train no: {self.trainNo} is running on time")
    
t = Rail(11217)
t.book("Mumbai", "Amritsar")
t.getFare("Mumbai", "Amritsar")
t.getStatus()
    