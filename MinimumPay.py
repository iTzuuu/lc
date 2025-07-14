days=int(input())
day_shift=list(map(int,input().split()))
night_shift=list(map(int,input().split()))
day_shift.sort()
night_shift.sort(reverse=True)
fourth=int(input())
cost=0
for i in range(days):
    hours=max(0,day_shift[i]+night_shift[i]-fourth)
    cost=cost+hours*100
print(cost)    
    