def isSafe(chessboard, row, col, n):
    for i in range(row):
        if chessboard[i][col] == 1:
            return False
    for j in range(n):
        if j != col and chessboard[row][j] == 1:
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if chessboard[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if chessboard[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def solveNQueens(chessboard, row, n):
    if row == n:
        return True
    for col in range(n):
        if isSafe(chessboard, row, col, n):
            chessboard[row][col] = 1
            if solveNQueens(chessboard, row + 1, n):
                return True
            chessboard[row][col] = 0
    return False

def nQueens(n):
    chessboard = [[0 for _ in range(n)] for _ in range(n)]
    return solveNQueens(chessboard, 0, n)

x = int(input("Enter the value of n: "))
print(nQueens(x))