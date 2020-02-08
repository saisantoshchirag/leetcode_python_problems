import time

def fibo1(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fibo1(n-1)+fibo1(n-2)


def fibo2(n):
    arr = [0,1]
    for i in range(n-2):
        arr.append(sum(arr[-2:]))
    print(len(arr))
    try:
        return arr[n]
    except:
        return arr[n-1]
start = time.clock()
#print(fibo1(50))
end = time.clock()
# print(end-start)

start1 = time.clock()
print(fibo2(100))
end1 = time.clock()
print(end1-start1)