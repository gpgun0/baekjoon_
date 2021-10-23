class Solution:
    def main(self):
        n = int(input())
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] % 10007 + 2*dp[i-2] % 10007
        
        return dp[n] % 10007

sol = Solution()
print(sol.main())