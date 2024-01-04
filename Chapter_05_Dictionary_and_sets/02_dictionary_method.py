myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'Sumit': 'Gamer'}
}

# Key function Title of the dict
# print(myDict.keys())

# Convert to list
# print(list(myDict.keys()))

#Typecasting
# print(type(myDict.keys()))

# Values of in the title 
# print(myDict.values())

# Items print (key,values) for all items is in proper manner.
# print(myDict.items())

#Update function 
updateDict = {
    "Friend": "Udith",
    "Game": "valorant"
}
myDict.update(updateDict)
print(myDict)

# GET function use in search
print(myDict.get("Game"))