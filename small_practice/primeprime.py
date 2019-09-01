import time

time_start = time.time()

primeList = [2]
for number in range(3,10000):
    flag = False
    for primeNumber in primeList:
        if number % primeNumber == 0:
            flag = False
            break
        else:
            flag = True
    if flag == True:       
        primeList.append(number)

time_end = time.time()
print('time cost',time_end-time_start,'s')