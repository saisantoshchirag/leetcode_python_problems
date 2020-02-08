def magic(mat):
    s = mat[0][0] + mat[1][1] + mat[2][2]
    s2 = mat[2][0] + mat[0][2]+ mat[1][1]
    if(s!=s2) : 
        return False
    for i in range(0, 3) : 
        rowSum = 0;      
        for j in range(0, 3) : 
            rowSum += mat[i][j] 
        if (rowSum != s) : 
            return False
    for i in range(0, 3): 
        colSum = 0
        for j in range(0, 3) : 
            colSum += mat[j][i] 
        if (s != colSum) : 
            return False
  
    return True
  

grid = [[4,3,8],[9,5,1],[2,7,6]]
print(sum(grid,[]))
print(magic(grid))
