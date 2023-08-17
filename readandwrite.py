f=open('C:/Users/Acer/OneDrive/Desktop/text.txt','r')
g=open('C:/Users/Acer/OneDrive/Desktop/text2.txt','w')
str=f.readline()
while str:
    g.write(str)
    str=f.readline()
f.close()
g.close()