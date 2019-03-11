m = eval(input("Please input a non negative number: "))
if m < 0:
    print("You made a mistake. Can't find the smallest output.")
else:
    n = int(m + 1)
    while n**2 > m:
        if (n-1)**2 <= m:
            print(n)
            break
        else:
            n -= 1
            continue