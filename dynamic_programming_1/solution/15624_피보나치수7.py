class Solution:
    def main(self):
        n = int(input())
        if not n:
            return 0

        dp = [0] + [1] + [0]*(n-1)

        for i in range(2, n+1):
            dp[i] = dp[i-1] % 1000000007 + dp[i-2] % 1000000007
        
        return dp[-1] % 1000000007 

sol = Solution()
print(sol.main())