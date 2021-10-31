class Solution:
    def main(self):
        n = int(input())
        if n == 0:
            return 1
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] % 1000000007 + dp[i-2] % 1000000007 + 1
        
        return dp[-1] % 1000000007

sol = Solution()
print(sol.main())