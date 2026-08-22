class Programmers:
    comapany = "Microsoft"
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        print("Creating object.......")
        
    def getInfo(self):
        print(f"The salary of {self.name} is {self.salary} working at {self.comapany}")
        
p1 = Programmers("Subodh", 350000)
p1.getInfo()
p2 = Programmers("Romeo", 100000)
p2.getInfo()