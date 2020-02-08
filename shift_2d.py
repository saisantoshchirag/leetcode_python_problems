import numpy as np
k =4
grid = [
        [3,8,1,9],
        [19,7,2,5],
        [4,6,10,11],
        [12,0,21,13]]
arr_t = sum(grid,[])

ar=[]
s = len(grid[0])
for item in grid:
    ar += item

for i in range(k):
#    print(ar)
#   ar = [ar.pop()] + ar
    ar = [ar[-1]] + ar[:-1]

print(ar)
print([[ar[i:i+len(grid[0])]] for i in range(0,len(ar),len(grid[0]))])
print(np.reshape(ar,(len(grid),len(grid[0]))))
