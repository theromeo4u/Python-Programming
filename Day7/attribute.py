class Attribute:
    name = "Romeo"
    def __init__(self,age):
        print("Creating object......")
        self.age = age
    def getInfo(self):
        
        print(f"My name is {self.name} and my age is {self.age}")
        
a = Attribute(27)
a.name = "Subodh"
a.getInfo()