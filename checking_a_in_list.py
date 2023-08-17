names=[]
c=0
for x in range(1,6):
    n=input("What is the name")
    names.append(n)
for y in names:
    for z in y:
        if 'a' in z:
            c = c + 1
print(c)

