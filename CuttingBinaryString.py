class Solution:
    def cuts(self,s):
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        powers_of_5 = set()
        # Precompute all powers of 5 up to the max possible value
        max_val = int('1' * n, 2)
        p = 1
        while p <= max_val:
            powers_of_5.add(bin(p)[2:])
            p *= 5
        for i in range(1, n + 1):
            for j in range(i):
                sub = s[j:i]
                if sub[0] == '0':
                    continue
                if sub in powers_of_5:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n] if dp[n] != float('inf') else -1
