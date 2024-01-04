# Write a program to create class

# class Number:
#     def sum(self):
#         return self.a + self.b
    
# num = Number()
# num.a = 12
# num.b = 34
# s = num.sum()
# print(s)

# Example Railway From

# class RailwayForm:
#     formType = "RailwayForm"
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.train}")

# sumitApplication = RailwayForm()
# sumitApplication.name = "Sumit Kumar Singh"
# sumitApplication.train = "Rajdhani Express"
# sumitApplication.printData()

# Game Development
# class Remote():
#     pass

# class Player:
#     def moveRight(self):
#         pass

#     def moveLeft(self):
#         pass
    
#     def moveTop(self):
#         pass

# remote1 = Remote()
# player1 = Player()

# if(remote1.isLeftpressed()):
#     player1.moveLeft()

# Class Attribute

# class Employees:
#    company = "Google"
#    salary = 100

# sumit = Employees()
# udith = Employees()
# sumit.salary = 300
# udith.salary = 400

# print(sumit.company)
# print(udith.company)
# Employees.company = "YouTube"
# print(sumit.company)
# print(udith.company)
# print(sumit.salary)
# print(udith.salary)

class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"play tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots a film")

    def speaks(self):
        print(self.name,"says how are you?")

tom = Human("tom cruise","actor")
tom.do_work()
tom.speaks()

sumit = Human("Sumit kumar singh","tennis player")
sumit.do_work()
sumit.speaks()
