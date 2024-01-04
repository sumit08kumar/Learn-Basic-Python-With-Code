#myDict = {
#    "Pankha": "Fan",
#    "Dabba": "Box",
#    "Vastu": "Item"
#}
#print("Options are", myDict.keys())
#a = input("Enter the hindi word\n")
# print("The meaning of your word is:", myDict[a])
# Below line will not throw an error if the keys is not present in the dictionary
# print("The meaning of your word is:", myDict.get(a))

# Write a program to input eight number from the user

# num1 = int(input("Enter the number\n"))
# num2 = int(input("Enter the number\n"))
# num3 = int(input("Enter the number\n"))
# num4 = int(input("Enter the number\n"))
# num5 = int(input("Enter the number\n"))
# num6 = int(input("Enter the number\n"))
# num7 = int(input("Enter the number\n"))
# num8 = int(input("Enter the number\n"))

# s = {num1, num2, num3, num4, num5, num6, num7, num8}
# print(s)

# Have a set with int and str as a values in it

# s = {18, "18"}
# print(s)

# Length of the following
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))

# Create an empty dictionary allow 4 friends to enter their favourite language name

favlang = {}

a = input("Enter the favorite language:\n ")
b = input("Enter the favorite language:\n ")
c = input("Enter the favorite language:\n ")
d = input("Enter the favorite language:\n ")
favlang[1] = a
favlang[2] = b
favlang[3] = c
favlang[4] = d

print(favlang)