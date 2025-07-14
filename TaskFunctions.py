stack = []
min_stack = []
n = int(input())
for _ in range(n):
    parts = input().split()
    if parts[0] == '0':
        x = int(parts[1])
        stack.append(x)
        if not min_stack or x <= min_stack[-1]:
            min_stack.append(x)
    elif parts[0] == '1':
        if stack:
            val = stack.pop()
            if min_stack and val == min_stack[-1]:
                min_stack.pop()
    elif parts[0] == '2':
        print(stack[-1] if stack else None)
    elif parts[0] == '3':
        print(min_stack[-1] if min_stack else None)
