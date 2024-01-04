# Write a program to print multiplication table.

#num = int(input("Enter the number"))
#for i in range(1,11):
#    # print(str(num) + "X" + str(i) + "=" + str(i*num))
#    print(f"{num} x {i}= {num*i}") # more simpler way 


# Write a program to greet all the person names stored in a list.

#l = ["Harry","Sahan","Sachin","Rahul"]
#for i in l:
#    if i.startswith("S"):
#        print("Hello " + i)

# Attempt multiplication using while loop

#num = int(input("Enter the number"))
#i = 1
#while i <= 10:
#    num = num * 1
#    print(f"{num} x {i} = {num*i}")
#    i +=1

# Write a program to find whether a given number is prime or not.

#num = int(input("Enter the number"))
#prime = True
#for i in range(2, num):
#    if(num%i == 0 and num!=2):
#        prime = False
#        break
#if prime:
#    print("This is the prime number")
#else:
#    print("THis is not prime number.")

# Write a program to find sum of first n natural number using while loop.

# num = int(input("Enter the number"))
# 
# if num < 0:
#    print("Enter a positive number")
# else:
#    sum = 0
#    # use while loop to iterate until zero
#    while(num > 0):
#        sum += num
#        num -= 1
#    print("The sum is", sum)

# Write the program to find factorial of any number

#num = int(input("Enter the number"))
#factorial = 1
#for i in range(1, num+1):
#   factorial = factorial * i
#   print(f"The factorial of this number is {factorial}")

# Write a program to print the following star:
#    *
#  * * *
# * * * * * 

#n = 3
#for i in range(3):
#   print(" " * (n-i-1), end="")
#   print("*" * (2*i+1), end="")
#   print(" " * (n-i-1))

# Write a program to print the following star:
#  *
#  * * *
#  * * * * 

# n = 4
# for i in range(4):
#    print("*" * (i+1))

# Write a program to multiply table in reverse order.

#table = int(input("Enter the table: "))

#limit = int(input("Enter the ending : "))

#for i in range(limit,0,-1):
#    print(i,"*",table,"=",i*table)

# Write a program to print the following star:

# * * *
# *   *
# * * *

n= int(input("Enter the number row and columns: "))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end="")
        else:
            print(" ", end="")
        print(" ")
    
