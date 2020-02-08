m = 3
n = 3
def op(mat,a,b):
    for i in range(a):
        for j in range(b):
            mat[i][j] += 1
    return mat

mat = [[0 for _ in range(m)] for _ in range(n)]
print(mat)
operations = [[2,2],[3,3]]
for a in operations:
    mat = op(mat,a[0],a[1])
print(mat)
s = sum(mat,[])
print(s)
