from math import factorial
n = 100
c = 0
prime = [1 for i in range(n+1)]
p=2
while p*p<=n:
    if prime[p]:
        for i in range(p*p,n+1,p):
            prime[i]=0
    p+=1
for p in range(2,n+1):
    if prime[p]:
        c+=1
print(c)
print((factorial(c)*factorial(n-c))%(1000000007))
