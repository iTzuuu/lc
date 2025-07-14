x = int(input())
nums = list(map(int, input().split()))
sum_no = int(input())
nums_set = set(nums)
count = 0
if sum_no == 0:
    for num in nums_set:
        if nums.count(num) > 1:
            count += 1
else:
    for num in nums_set:
        if num + sum_no in nums_set:
            count += 1
print(count)