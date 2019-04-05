from time import time
import random


def merge(a, b):
    L = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            L.append(a[i])
            i += 1
        else:
            L.append(b[j])
            j += 1   
    for k in range(i, len(a)):
        L.append(a[k])
    for k in range(j, len(b)):
        L.append(b[k])
    return L

def mergeSort(a):
    n = len(a)
    if n == 1:
        return a
    k = int(n/2)
    b = mergeSort(a[:k])
    c = mergeSort(a[k:])
    L = merge(b, c)
    return L


n = 10000
a = []
for i in range(n):
    a.append(random.randint(0,10000))

startime  = time()
mergeSort(a)
endtime = time()
print("Time:", endtime-startime)