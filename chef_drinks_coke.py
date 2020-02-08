for iter in range(int(input())):
    n,m,k,l,r = map(int,input().split())
    c = list()
    p = list()
    for iter in range(n):
        ci,pi = map(int,input().split())
        for run in range(m):
            if ci < k-1:
                ci += 1
            elif ci > k+1:
                ci -= 1
            else:
                ci = k
        if ci >= l and ci <=r:
            p.append(pi)
    if len(p) != 0:
        print(min(p))
    else:
        print(-1)
        
