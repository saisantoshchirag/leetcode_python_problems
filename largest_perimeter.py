a = [2,1,1]
a.sort()
a = a[::-1]
print(a)
for i in range(2,len(a)):
    if a[i-1]+a[i] > a[i-2]:
        print(a[i]+a[i-1]+a[i-2])
        
    
