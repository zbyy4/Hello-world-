def binarySearch(L, num, low, high):
    if low > high:
        return low
    mid  = (low + high)//2

    if L[mid] == num:
        return mid
    elif L[mid] < num:
        return binarySearch(L, num, mid+1, high)
    else:
        return binarySearch(L, num, low, mid-1)

def binaryinsert(L, m):
    k = binarySearch(L, m, 0, len(L)-1)
    L.insert(k, m)
    return L

a = [-1, 4, 9, 45, 50, 78, 93, 120, 149, 191, 200, 201]
print(binaryinsert(a, 3))