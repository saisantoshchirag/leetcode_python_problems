arr = [1,2,3,5,6,8,9,10,11,12,15,17,]
print(arr)
i=0
j=0
while(i<n):
    j = i
    while(j+1<n and arr[j+1]==arr[j]+1):
        j+=1
    if i==j:
        print(arr[i])
        i+=1
    else:
        print(arr[i],'-',arr[j],end=" ")
        i= j+1
        
