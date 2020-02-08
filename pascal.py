from math import factorial as fact
ar = [[1]]
n = 5
for i in range(1,n+1):
    t = []
    for j in range(i+1):
        t.append((fact(i))/(fact(j)*fact(i-j)))
    ar.append(t)
print(ar)
