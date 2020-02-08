import math
t = 1
for i in range(t):
    n,a,b,c = map(int,input().split())
    # n,a,b,c = 3,1,5,2
    arr = list(map(int,input().split()))
    # arr = [1000000000]
    mi = math.inf
    for i in arr:
        mi = min(abs(i-b)+abs(i-a)+c,mi)
    print(mi)