from math import sin, cos, tan

# Input part
print("sin = 's', cos = 'c', tan = 't'")
while True:
    f = input("Please choose the function: ")
    if f not in ['s', 'c', 't']:
        print("You made a mistake.")
        continue
    break
while True:
    try:
        a = eval(input("Please input the start point: "))
        break
    except:
        print("You made a mistake.")   
while True:
    try:
        b = eval(input("Please input the end point: "))
        if b > a:
            break
        else:
            print("The end point should be bigger.")
    except:
        print("You made a mistake.")
while True:
    try:
        n = int(input("Please input the number of sub-intervals: "))
        if n <= 0:
            print("It should greater than 0.")
            continue
        break
    except:
        print("It should be an integer.")
# Calculation part
result = 0
if f == 's':
    for i in range(1,n+1):
        width = (b-a)/n
        x = a + width*(i-0.5)
        height = sin(x)
        result += width*height
elif f == 'c':
    for i in range(1,n+1):
        width = (b-a)/n
        x = a + width*(i-0.5)
        height = cos(x)
        result += width*height
else:
    for i in range(1,n+1):
        width = (b-a)/n
        x = a + width*(i-0.5)
        height = tan(x)
        result += width*height
print("The result of numerical intergation is:", result) 