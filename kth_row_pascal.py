from math import factorial as fct
n = 4
ar = []
for i in range(n+1):
    num = int(fct(n)/(fct(i)*fct(n-i)))
    ar.append(num)
print(ar)
