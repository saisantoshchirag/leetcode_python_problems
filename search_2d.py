def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return True

        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False

print(binarySearch([1],0,1,1))
o = []
#m = [
# [1,3,5,7],
#  [10,11,16,20],
#   [23,30,34,50],
#    ]
m = [[1]]
t = 1
for i in range(len(m)):
    if m[i][0] <= t and m[i][-1] >= t:
        print(True)
        s = binarySearch(m[i],0,len(m[i]),t)
        o.append(s)
    else:
        o.append(0)
print(o)

print(any(o))
