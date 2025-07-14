x, y = map(int, input().split())
x1 = []
for i in range(x):
    row = list(map(int, input().split()))
    x1.append(row)
x2 = []
for i in range(x):
    row = list(map(int, input().split()))
    x2.append(row)
sum_matrix = [[x1[i][j] + x2[i][j] for j in range(y)] for i in range(x)]
print("First Matrix:")
for row in x1:
    print(*row)
print("Second Matrix:")
for row in x2:
    print(*row)
print("Sum of the two matrices is:")
for row in sum_matrix:
    print(*row)