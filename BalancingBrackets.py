x = input().strip()
stack = []
balanced = True
for c in x:
    if c == '{':
        stack.append(c)
    elif c == '}':
        if not stack:
            balanced = False
            break
        stack.pop()
if balanced and not stack:
    print("Matching")
else:
    print("Not Matching")