n = 30
prime = [1 for i in range(n+1)]
p=2
while p*p<=n:
    if prime[p]:
        for i in range(p*p,n+1,p):
            prime[i]=0
    p+=1
for p in range(2,n):
    if prime[p]:
        print(p)
