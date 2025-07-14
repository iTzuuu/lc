def powerSum(X, N):
    def countWays(total, num, path):
        val = num ** N
        if val > total:
            return 0
        if val == total:
            print("Combination:", path + [num])
            return 1
        # Include num or skip num
        return countWays(total - val, num + 1, path + [num]) + countWays(total, num + 1, path)
    return countWays(X, 1, [])

if __name__ == "__main__":
    X = int(input())
    N = int(input())
    print("Total ways:", powerSum(X, N))
