myRange = []
y=int(input("How many numbers to product"))
c=0
num=1
while c < y:
    z=int(input("What is the number"))
    myRange.append(z)
    c+=1
for i in myRange:
    num*=i
print(num)

