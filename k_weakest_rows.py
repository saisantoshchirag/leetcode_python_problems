mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
arr = []
for i in range(len(mat)):
    arr.append([mat[i].count(1),i])
print(arr)
arr = sorted(arr,key=lambda x: (x[0],x[1]))