x = int(input())
nums = list(map(int, input().split()))
sum=0
for num in nums:
    sum+=num
print((x*(x+1)//2)-sum)