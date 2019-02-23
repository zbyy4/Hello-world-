hours = input("Please enter your work hours: ")
n = 2
while n > 1:
    try:
        hours = float(hours)
        n = n - 1
    except:
        print("Fuck you!")
        hours = input("Please enter again: ")
        continue
rate = input("Please enter your hourly rate: ")
while n > 0:
    try:
        rate = float(rate)
        n = n-1
    except:
        print("You mother fucker!")
        rate = input("Please enter again: ")
        continue
if hours <= 40 :
    print("Your pay is " + str(hours*rate))
else:
    print("Your pay is " + str((hours-40)*1.5*rate+40*rate))