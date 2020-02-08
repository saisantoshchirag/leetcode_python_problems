import matplotlib.pyplot as plt
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(mat)
#for nxn matrix
for i in range(len(mat)):
    for j in range(i,len(mat[i])):
        mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

print(mat)
for j in range(len(mat)):
    mat[j] = mat[j][::-1]
print(mat)

m = [[1,2,3],[4,5,6]]
s = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print(s)
