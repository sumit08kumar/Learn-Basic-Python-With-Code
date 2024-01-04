# Finding percentage using functions.

# def percent(marks):
#     p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
#     return p
# 
# marks1 = [45, 57, 86, 77]
# percentage1 = percent(marks1)
# 
# marks2 = [75, 69, 98, 65]
# percentage2 = percent(marks2)
# print(percentage1, percentage2)
# 
#Another Method to perform the percentage method

# marks = [45, 57, 86, 77]
# percentage1 = (sum(marks)/400)*100
# 
# marks2 = [75, 69, 98, 65]
# percentage2 = (sum(marks2)/400)*100
# print(percentage1, percentage2)

# Write a program to greet a user with "Good Day" using functions.

# def greet(name):
#    print("Good Day, " + name)

#greet("Sumit")

# Function with arguments

#def greet(name):
#    print("Good Day, " + name)

#def mySum(num1, num2):
#    return num1 + num2

#greet("Sumit")
#s = mySum(6, 32)
#print(s)

#greet("Sumit")

# Default Parameter Value

def greet(name="Stanger"):
   print("Good Day, " + name)

greet("Sumit")
greet()
