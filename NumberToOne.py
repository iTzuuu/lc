x=int(input())
def min_steps_to_one(n, memo={}):
    if n == 1:
        return 0
    if n in memo:
        return memo[n]
    steps = min_steps_to_one(n - 1, memo) + 1
    if n % 2 == 0:
        steps = min(steps, min_steps_to_one(n // 2, memo) + 1)
    if n % 3 == 0:
        steps = min(steps, min_steps_to_one(n // 3, memo) + 1)
    memo[n] = steps
    return steps

print(min_steps_to_one(x))