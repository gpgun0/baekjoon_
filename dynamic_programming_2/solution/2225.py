class Solution:
    def main(self, n, k):
        for i in range(1, k+1):
            for j in range(0, n+1):
                if i == 1:
                    dp[i][j] = 1
                    continue

                for l in range(0, j+1):
                    dp[i][j] += dp[i-1][j-l] % 1000000000 
        
        return dp[k][n] % 1000000000

sol = Solution()
n, k = map(int, input().split())
dp = [[0]*(n+1) for _ in range(k+1)]
print(sol.main(n, k))