arr = [17,18,5,4,6,1]
arr1 = []
for i in range(len(arr)-1):
    arr1.append(max(arr[i+1:]))
arr1.append(-1)
print(arr1)
