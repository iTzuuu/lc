k = int(input("Enter the value of k: "))
chessboard = [[0 for _ in range(k)] for _ in range(k)]
def isAttacking(i, j):
    for x in range(k):
        if chessboard[i][x] == 1 or chessboard[x][j] == 1:
            return True
    for l in range(k):
        for m in range(k):
            if l + m == i + j and chessboard[l][m] == 1:
                return True
            if l - m == i - j and chessboard[l][m] == 1:
                return True
    return False

def nQueens(row):

    if row == k:
        return True
    for col in range(k):
        if not isAttacking(row, col) and chessboard[row][col] == 0:
            chessboard[row][col] = 1
            if nQueens(row + 1):
                return True
            chessboard[row][col] = 0
    return False

def printChessboard():
    for row in chessboard:
        print(' '.join('Q' if x == 1 else '.' for x in row))

if nQueens(0):
    printChessboard()
    print(True)
else:
    print(False)