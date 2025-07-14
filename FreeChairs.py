x = input()
ch = 0
free = 0
for c in x:
    if c == 'C' or c == 'U':
        if free > 0:
            free -= 1
        else:
            ch += 1
    else:
        free += 1
print(ch)