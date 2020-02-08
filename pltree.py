arr = [2,4,7]
c = 0
for i in arr:
    if i+1 not in arr or i-1 not in arr:
        c+=1
print(c)
