nums = list(map(int, input().replace(',', ' ').split()))
if not nums:
    print(0)
else:
    max_p = 0
    min_p = nums[0]
    for price in nums[1:]:
        if price - min_p > max_p:
            max_p = price - min_p
        if price < min_p:
            min_p = price
    print(max_p)
