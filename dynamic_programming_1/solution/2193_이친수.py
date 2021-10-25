class Solution:
    def main(self):
        n = int(input())
        dp = [0]*(n+1)

        for i in range(1, n+1):
            if i <= 2:
                dp[i] = 1
            else:
                dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

sol = Solution()
print(sol.main())