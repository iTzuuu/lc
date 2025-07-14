x = int(input())
showtiming = []
for i in range(x):
    showtiming.append(list(map(int, input().split())))
showtiming.sort(key=lambda x: (x[1], x[0]))    
count = 1
last_end_time = showtiming[0][1]
for i in range(1, x):
    if showtiming[i][0] >= last_end_time:
        count += 1
        last_end_time = showtiming[i][1]
print(count)