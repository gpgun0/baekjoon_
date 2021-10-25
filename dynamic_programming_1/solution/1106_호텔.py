class Solution:
    def main(self):
        c, n = map(int, input().split())
        cost = [0]*(n+1)
        effect = [0]*(n+1)
        dp = [[0] + [1e9]*(c) for _ in range(n+1)]

        for i in range(1, n+1):
            cost[i], effect[i] = map(int, input().split())
        
        for i in range(1, n+1):
            for j in range(1, c+1):
                if effect[i] >= j:
                    dp[i][j] = min(dp[i-1][j], cost[i])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-effect[i]] + cost[i])
        
        return dp[n][-1]

sol = Solution()
print(sol.main())