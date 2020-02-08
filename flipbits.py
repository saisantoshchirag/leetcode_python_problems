import math
n=1
x = len(bin(n)[2:]) 
for i in range(0, x):  
    n = (n ^ (1 << i))
print(n) 
