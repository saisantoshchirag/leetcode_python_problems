def pairs(k, arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if abs(arr[j]-arr[i]) == 1:
                count+=1
    return count
