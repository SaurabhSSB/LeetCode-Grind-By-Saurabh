class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
        return dp[n]
