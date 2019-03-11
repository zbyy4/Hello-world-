number = int(input("Enter an integer: "))
# Avoid to print the minus sign.
if number < 0:
    number = -number
number = str(number)
for i in number:
    print(i)