class Solution:
    def main(self):
        n, k = map(int, input().split())
        dp = [[1]*(n+1) for _ in range(k+1)]

        for i in range(1, k+1):
            for j in range(1, n+1):
                if i == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

        return dp[k][n] % 1000000000

sol = Solution()
print(sol.main())