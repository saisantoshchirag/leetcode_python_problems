arr = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(arr)
i,j=1,1
flag = True
while ((arr[j+1]-arr[j])/(arr[i+1]/arr[i]) == (arr[j]-arr[j-1])/(arr[i]/arr[i-1])):
    print(flag)
    i+=1
    j+=1
    if i==len(arr)-2:
        break
    
