def isvalid(row):
    return len(set(row)) == len(row)
def validSolution(board):
    print(board)
    for i in board:
        if not(isvalid(i)):
            return False
    for i in range(len(board)):
        for j in range(i,len(board[i])):
            board[i][j],board[j][i] = board[j][i],board[i][j]
    for i in board:
        if not(isvalid(i)):
            return False
    #need to check all 9 boxes
    if board[0][1] == board[1][0]:
        return False
    return True