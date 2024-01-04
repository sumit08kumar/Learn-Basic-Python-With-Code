# Write a program to read the text from the given file 'poems.txt'.

# f = open('E:\Python\Chapter_09_File-IO.py\poems.txt')
# t = f.read()
# if 'twinkle' in t:
#     print("twinkle is present")
# else:
#     print("twinkle is not present")

# f.close()

# Write a program to build a game function.

# def game():
#     return 564
 
# score = game()
# with open("E:\Python\Chapter_09_File-IO.py\highscore.txt") as f:
#     highscore = int(f.read())

# if highscore < score:
#     with open("highscore.txt", "w") as f:
#         f.write(str(score))

# Write a program to generate multiplication tables from 2 to 20.

# for i in range(2, 21):
#     with open(f"E:\Python\Chapter_09_File-IO.py\Multiplication_table{i}.txt", "w") as f:
#         for j in range(1, 11):
#             f.write(f"{i} x {j} = {i*j}")
#             if j != 10:
#                 f.write('\n')

# Write a program that update the text in the file.

# with open("E:\Python\Chapter_09_File-IO.py\sample2.txt") as f:
#    content = f.read()

# content = content.replace("Donkey", "$%^&@$")

# with open("sample2.txt", "w") as f:
#     f.write(content)

# Write a program to update list of words as in previous example.

# words = ["donkey", "mote", "Ponkey"]

# with open("E:\Python\Chapter_09_File-IO.py\sample2.txt") as f:
#     content = f.read()

#for word in words:
#     content = content.replace(word, "$%^&@#$")

# with open("sample2.txt", "w") as f:
#     f.write(content)

# Write a program to read a log file which content python string.

# with open("E:\Python\Chapter_09_File-IO.py\log.txt") as f:
#     content = f.read()

# if 'python' in content.lower():
#     print("Yes python is present")
# else:
#     print("No python is not present")

# Write a program to find the line in which python has been written.

#content = True
# i = 1
# with open("E:\Python\Chapter_09_File-IO.py\log.txt") as f:
#     while content:

#         content = f.readline()

#         if 'python' in content.lower():
#             print(content)
#             print("Yes python is presented")
#             print(i)
#         i+=1

# Write a program to make a copy of a text file 'this.txt'.

with open('E:\\Python\\Chapter_09_File-IO.py\this.txt', 'r') as f:
    content = f.read()

with open('copy.txt', 'w') as f:
    f.write(content)





