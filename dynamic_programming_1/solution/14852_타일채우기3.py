class Solution:
    def main(self):
        n = int(input())

        dp = [0] + [2] + [7] + [22] + [0]*(n-3)
        
        if n <= 2:
            return dp[n]

        for i in range(4, n+1):
            dp[i] = ((dp[i-1]*2) % 1000000007 + (dp[i-2]*3) % 1000000007 + (dp[i-3]*2) % 1000000007) % 1000000007
        
        return dp[-1] % 1000000007


sol = Solution()
print(sol.main())