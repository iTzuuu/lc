n = int(input())
m = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
count = 0
row, col = 0, m - 1
while row < n and col >= 0:
    if mat[row][col] < 0:
        count += col + 1
        row += 1
    else:
        col -= 1
print(count)
