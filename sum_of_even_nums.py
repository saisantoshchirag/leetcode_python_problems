a = [1,2,3,4]
que = [[1,0],[-3,1],[-4,0],[2,3]]
out = []
for i in range(len(que)):
    a[que[i][1]] += que[i][0]
    out.append(sum([i for i in a if i%2==0]))
print(a)
print(out)    
