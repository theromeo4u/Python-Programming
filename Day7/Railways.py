import random


class Rail:
    def book(self):
        print(f"Ticket is booked on {self.trainNo} from {self.From} to {self.To}")
    
    def getFare(self,trainNo,From,To):
        self.trainNo = trainNo
        self.From = From
        self.To = To
        print(f"Ticket Fare of train no: {self.trainNo} from {self.From} to {self.To} is {random.randint(100,999)}")

    def getStatus(self, trainNo):
        print(f"Status of train no: {trainNo} is running on time")
        