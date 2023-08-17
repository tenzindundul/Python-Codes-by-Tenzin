temp = { "sun":77, "mon":88,"tue":60, "wed":65}
moderate = []
for k,y in temp.items():
    if(y>=70 and y<=80):
        moderate.append(k)
print(moderate)