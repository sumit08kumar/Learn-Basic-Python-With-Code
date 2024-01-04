# Write a program using function to find grestest of three numbers.

# def maximun(num1, num2, num3):
#     if (num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#            return num3
#     else:
#      if(num2>num3):
#        return num2
#      else: 
#         return num3
     
# m = maximun(23, 25, 54)
# print("The value of the maximunis " + str(m))

# Write a program to convert Celsius to Farenheit

# def farh(cel):
#   return (cel*(9/5)) + 32

# c = 30
# f = farh(c)
# print("Fahreheit temperture is " + str(f))

# Write a program to prevent a python print() function

# print("Hello", end= " ")
# print("How", end= " ")
# print("Are", end= " ")
# print("You", end= " ")

# def recurSum(n):
#    if n <= 1:
#        return n
#    return n + recurSum(n - 1)
  
# n = 3
# print(recurSum(n))

# Write a program to print the following star patterns

# n = 6

# for i in range(n):

#   print("*" * (n-i))

# Write a program which convert inches into cms

# Inches=int(input("Enter the length in Inches:"))  

# centimeter  = 2.54 * Inches;    
     
# print("The length in centimeter",round(centimeter,2))  

# Write a program to print the to remove a given word from the list and stip it at the same time.

# this = "    Sumit Valo    "
# print(this.strip())


# def remove_and_strip(string, word):
#     newStr = string.replace(word, "")
#     return newStr.strip()

# this = "   Sumit Singh   "
# n = remove_and_strip(this, "Singh")
# print(n)

# Write a function to print multiplication table of a given number.

def multi(n):
    for i in range(1,11):
        print(n," x ", i, " = ", n*i)

n = int(input("Enter the number"))
multi(n)
    