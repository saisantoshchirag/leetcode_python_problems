mat = [[0,1,2,0],[3,4,5,2],[1,3,5,1]]
col,row = [],[]
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 0:
            col.append(i)
            row.append(j)
print(row)
print(col)
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if j in row or i in col:
            mat[i][j] = 0
print(mat)
