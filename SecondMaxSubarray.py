x = int(input())
y = int(input())
tastiness = list(map(int, input().split()))
mt = float('-inf')
smt = float('-inf')
for i in range(x - y + 1):
    ct = sum(tastiness[i:i + y])
    if ct > mt:
        smt = mt
        mt = ct
    elif mt > ct > smt:
        smt = ct
print(mt)
print(smt if smt != float('-inf') else "No second maximum")
if mt == smt or smt == float('-inf'):
    print("No second maximum")
