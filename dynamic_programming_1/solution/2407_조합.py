class Solution:
    def main(self):
        n, m = map(int, input().split())
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(i+1):
                if j == 0 or j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

                if i == n and j == m:
                    return dp[i][j]

sol = Solution()
print(sol.main())