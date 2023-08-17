import math
num = int(input("enter number to compute factorial of:"))
valid_input =  False
while not valid_input:
    try:
        result=math.factorial(num)
        print(result)
        valid_input = True
    except ValueError:
        print("Campt compute the factorial of negaive number")
        num= int(input("Please re-enter"))