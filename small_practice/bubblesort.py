a = [45, 3, -1, 35, -11, 92, 2, -4, 3, 93, 2, 0, -2, -4]
length = len(a)
for k in range(length-1):
    length -= 1
    for i in range(length):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
print(a)