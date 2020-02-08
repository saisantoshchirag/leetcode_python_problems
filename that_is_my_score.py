def func(k):
    out = {}
    for i in range(len(k)):
        if k[i][0] not in out:
            out[k[i][0]] = k[i][1]
        else:
            if out[k[i][0]] < k[i][1]:
                out[k[i][0]] = k[i][1]
    n = 0
    for i in out:
        if i <= 8:
            n+=out[i]
    return n
for _ in range(int(input())):
    n = int(input())
    k = []
    for i in range(n):
        s = list(map(int,input().split()))
        k.append(s)
    print(func(k))
    
