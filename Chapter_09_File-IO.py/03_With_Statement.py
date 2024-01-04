''' with open('Sample2.txt', 'r') as f:
    a = f.read()
with open('Sample2.txt', 'w') as f:
    a = f.write("Yes")
print(a) '''

''' word_stats={}

with open("E:\Python\Chapter_09_File-IO.py\peom.txt","r") as f:
    for line in f:
        words=line.split(' ')
        for word in words:
            if word in word_stats:
                word_stats[word]+=1
            else:
                word_stats[word] = 1

    print(word_stats)

    word_occurances = list(word_stats.values())
    max_count = max(word_occurances)
    print("Max occurances of any word is:",max_count)

    print("Words with max occurances are: ")
    for word, count in word_stats.items():
        if count==max_count:
            print(word) '''

with open("Chapter_09_File-IO.py/stock.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    next(f)  # This will skip first line in the file which is a header
    for line in f:
        tokens = line.split(",")
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price / eps, 2)
        pb = round(price / book, 2)
        out.write(f"{stock},{pe},{pb}\n")

