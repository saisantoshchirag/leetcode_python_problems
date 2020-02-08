import math
n = 1
c = 0
while n!=1:
    c+=1
    x = math.log2(n)
    if x==int(x):
        n = n//2
    else:
        n -= (2**int(x))
print(c)
