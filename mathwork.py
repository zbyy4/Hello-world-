import math

def comb(n,m):
    return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))



n = 0
for i in range(0,5):
    c = comb(100,i)
    n += c*(0.05**i)*(0.95**(100-i))*(5-i)*700

print(n)