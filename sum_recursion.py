def binarySum(L, low, high):
    mid = (low + high)//2
    if low > high:
        return 0
    if low == high:
        return L[low]
    if low+1 == high:
        return L[low] + L[high]
    return binarySum(L, low, mid-1) + binarySum(L, mid, high)

a = [1,2,3,4,5]
print(binarySum(a,0,len(a)-1))