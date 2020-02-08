def flip_horiz(mat):
    for i in range(len(mat)):
        mat[i] = mat[i][::-1]
    return mat

def invert(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]==1:
                mat[i][j] = 0
            elif mat[i][j]==0:
                mat[i][j] = 1
    return mat
mat = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(mat)
mat = flip_horiz(mat)
print(mat)
mat = invert(mat)
print(mat)
