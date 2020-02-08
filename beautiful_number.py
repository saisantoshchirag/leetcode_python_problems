t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(10**(n-1),10**n):
        num,sol = 0,-1
        if '0' in str(i):
            continue
        for j in str(i):
            num+=int(j)**2
        if num**0.5==int(num**0.5):
            sol = i
            break
    print(sol)
