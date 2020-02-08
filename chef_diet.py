t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    i,c=0,0
    while i<len(l):
        if sum(l[:i+1]) >= k*(i+1):
            c+=1
            i+=1
        else:
            break
    if c==len(l):
        print('YES')
    else:
        print('NO ',c+1)
