#Wrie a Python programme to convert temperatue to and from Celsius, Fehrenheit
def f_to_c(f):
    c=(f-32)*5/9
    print(c)
def c_to_f(c):
    f= (c*9/5)+32
    print(f)

x= input("Enter 'A' to convert Celious to Fehrenheit and 'B' to convert Fehrenheit to Celcius \n:")
if x=="A":
    x=int(input("What is the value of Celius"))
    c_to_f(x)
elif x=="B":
    y = int(input("What is the value of Frenheit"))
    f_to_c(y)
