dict = {"-...": "B", ".-" : "A", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F","--.": "G","....": "H" }
lst = []
e = int(input("Enter the number"))
for i in range(0,e):
    word = input("Enter the word")
    if(word in dict.keys()):
        lst.append(dict.values())
for l in lst:
    print(l)