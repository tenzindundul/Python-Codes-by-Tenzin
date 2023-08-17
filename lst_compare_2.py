lst1=[]
lst2=[]
for x in range(1,4):
    x=int(input("What is the number in lst 1"))
    lst1.append(x)
for x in range(1,4):
    y = int(input("What is the number in lst 2"))
    lst2.append(y)
if len(lst1)==len(lst2):
    print("Same length")
else:
    print("Not same")
if sum(lst1)==sum(lst2):
    print("same sum")
else:
    print("Not same")
for i in lst1:
    if i in lst2:
        print("same item is ",i)
