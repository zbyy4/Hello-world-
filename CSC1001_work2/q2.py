# Generate the prime-number list.
primeList = [2]
for number in range(3, 9942):
    flag = False
    for primeNumber in primeList:
        if number % primeNumber == 0:
            flag = False
            break
        else:
            flag = True
    if flag == True:       
        primeList.append(number)
# Pick emirp number out from the prime-number list.
emirpList = []
for primeNumber in primeList:
    primeNumber = str(primeNumber)
    palindromic = primeNumber[::-1]
    if palindromic == primeNumber:
        continue
    elif eval(palindromic) in primeList:
        emirpList.append(str(primeNumber).ljust(5))
# Print out the table.
for index in range(0,91,10):
    print(" ".join(emirpList[index:index+10]))