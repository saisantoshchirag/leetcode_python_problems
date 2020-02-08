def func(k):
    n = 0
    for i in range(len(k)):
        for j in range(i+1,len(k)):
            if k[i]+k[j] == k[i]*k[j]:
                n+=1
    return n


for _ in range(int(input())):
    n = int(input())
    k = list(map(int,input().split()))
    print(func(k))
