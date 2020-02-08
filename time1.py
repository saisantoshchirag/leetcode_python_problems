from time import clock
import random
from time import time
from math import factorial
def su(arr):
    s = 0
    for i in arr:
        s+=i
    return s

s = [random.randint(0,100000000) for _ in range(10000000)]

a1 = time()
# print('inbuit sum')
#print(sum(s))
b1 = time()
# print(b1-a1)

a1 = time()
# print('o(n)')
# print(su(s))
b1 = time()
# print(b1-a1)

def fact1(num):
    return factorial(num)

def fact2(num):
    n = 1
    for i in range(1,num):
        n*=i
    return n

a2 = time()
# print('inbuilt factorial')
# f1 = [fact1(i) for i in s]
b2 = time()
# print(b2-a2)

a2 = time()
# print('o(n)')
# f2 = [fact2(i) for i in s]
b2 = time()
# print(b2-a2)


def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


s=sorted(s)
def linearSearch(arr,num):
    for i in arr:
        if i==num:
            print(num)
            return i
    return -1

#best worst case
n = s[-1]
print('n',n)
a3 = time()
print('binary search')
print(linearSearch(s,n))
b3 = time()
print(b3-a3)

a4 = time()
print('linear search')
print(linearSearch(s,n))
b4 = time()
print(b4-a4)