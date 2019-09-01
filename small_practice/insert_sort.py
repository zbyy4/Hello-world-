a = [45, 3, -2, 78, 45, 2, -2, 91, 9, -100, 99, 23, 1888, 293, 19, -3]
b = []
for i in a:
    k = 0
    for j in b:
        if i <= j:
            break
        k += 1
    b.insert(k, i)
print(b)