nums = list(map(int, input().replace(',', ' ').split()))
if not nums:
    print(0)
else:
    max_profit = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            max_profit += nums[i] - nums[i-1]
    print(max_profit)
