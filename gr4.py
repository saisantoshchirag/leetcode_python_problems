from sys import stdin,stdout


n,q = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))
for i in range(q):
    r = -1
    l,x = map(int,stdin.readline().split())
    for i in range(l,len(arr)):
        if min(arr[l:i+1])<x:
            r=i
            break
    stdout.write(str(r))
