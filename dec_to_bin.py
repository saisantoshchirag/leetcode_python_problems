t = int(input())
for a in range(t):
    n,num = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    temp = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]==arr[j]:
                continue
            if arr[i] + arr[j] <num:
                if arr[i] + arr[j] > temp:
                    temp = arr[i]+arr[j]
                    final = []
                    final.append([min(arr[i],arr[j]),max(arr[i],arr[j])])
    print(final[0][0],final[0][1])
