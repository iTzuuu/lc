class Solution:
    def maxGold(self, mat):
        if not mat or not mat[0]:
            return 0
        n = len(mat)
        m = len(mat[0])
        dp = [[0]*m for _ in range(n)]
        for row in range(n):
            dp[row][m-1] = mat[row][m-1]
        for col in range(m-2, -1, -1):
            for row in range(n):
                right = dp[row][col+1]
                right_up = dp[row-1][col+1] if row > 0 else 0
                right_down = dp[row+1][col+1] if row < n-1 else 0
                dp[row][col] = mat[row][col] + max(right, right_up, right_down)
        return max(dp[row][0] for row in range(n))