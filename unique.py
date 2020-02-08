def findSingle(ar): 
      
    res = ar[0]  
    for i in range(1,len(ar)):
        res = res ^ ar[i]
    return res

ar = [1,2,3,4,5,3,2,4,5]
print(findSingle(ar))

num = 2
print(int(num**(1/4))==num**(1/4))
