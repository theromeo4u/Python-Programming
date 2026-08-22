class Calculator:
    def __init__(self,radius):
        self.radius = radius
        
    def square(self):
        ans = self.radius * self.radius
        print(f"The square of {self.radius} is {ans}")
        
    def cube(self):
        ans = self.radius * self.radius * self.radius
        print(f"The Cube of {self.radius} is {ans}")
    def squareroot(self):
            ans = self.radius ** 1/2
            print(f"The squareroot of {self.radius} is {ans}")        
num = int(input("Enter a number for Square, Squareroot and Cube: "))

c = Calculator(num)
c.square()
c.cube()
c.squareroot()