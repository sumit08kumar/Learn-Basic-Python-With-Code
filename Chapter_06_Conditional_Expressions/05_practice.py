# Write a program to find greatest of four number entered by user

# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))
# num3 = int(input("Enter the number: "))
# num4 = int(input("Enter the number: "))

# if(num1 > num4):
#     f1 = num1
# else:
#     f1 = num4

# if(num2 > num3):
#     f2 = num2
# else:
#     f2 = num3

# if(f1 > f2):
#     print(str(f1) + " is greatest")
# else:
#     print(str(f2) + " is greatest")

# Write a program to find out whether a student is pass or fail 

# sub1 = int(input("Enter first subject marks\n"))
# sub2 = int(input("Enter first subject marks\n"))
# sub3 = int(input("Enter first subject marks\n"))

# if(sub1 < 33 or sub2 < 33 or sub3 < 33):
#     print("You are fail because you have less than 33% in one of the subjects")

# elif(sub1 + sub2 + sub3)/3 < 40:
#     print("You are fail due to total percentage less than 40")
#  else:
#      print("Congatulations! You passed the exam.")
# 
#  Spam comment is defined as a lot containing 

# text = input("Enter the text")
# spam = False
 
# if("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This text is spam")
# else:
#     print("This text is not spam")

# Write a program to find whether a given username contains les than 10 charachter or not

# names = ["harry", "subham", "rohit", "aditi",]
# name = input("Enter the name to check\n")

# if name in names:
#     print("Your name is present in the list")
# else:
#     print("Your name is not present in the list")

# Write a program to calculate the grade of a student from his marks.

# marks = int(input("Enter Your Marks\n"))

# if marks >= 90:
#     grade = "Ex"
# elif marks >= 80:
#     grade = "A"
# elif marks >= 70:
#     grade = "B"
# elif marks >= 60:
#     grade = "C"
# elif marks >= 50:
#     grade = "D"
# else:
#     grade = "F"
 
# print("Your grade is " + grade)

# Write a program to find out whether a given post is talking about "Harry" or not.

post = input("Enter the post: ")
if("Harry" in post):
    print("Yes")
elif("harry" in post):
    print("Yes")
else:
    print("No")