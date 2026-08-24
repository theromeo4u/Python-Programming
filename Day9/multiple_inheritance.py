class Employee:
    company = "Meta"
    def __init__(self,name , salary,language):
        self.name = name
        self.salary = salary
        self.language = language
    def getInfo(self):
        print(f"The name of the company is {self.company} and salary is {self.salary}")
    
class Coder:    
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee,Coder):
    def printLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
   
   
# a = Employee("Romeo",60000,"Python")
b = Programmer("Subodh", 50000,"Java")
b.getInfo()        
b.showLanguage()
b.printLanguage()