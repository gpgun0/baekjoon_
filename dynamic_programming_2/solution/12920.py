class Solution:
    def main(self):
        for i in range(1, n+1):
            for j in range(1, m+1):
                if j < weight[i]:
                    dp[i][j] = dp[i-1][j]
                    continue

                if count[i]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j - weight[i]] + value[i])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i], dp[i][j-1])
                
                count[i] = max(0, count[i] - 1)
        print(dp)
sol = Solution()
n, m = map(int, input().split())
weight = [0]*(n+1)
value = [0]*(n+1)
count = [0]*(n+1)

for i in range(1, n+1):
    weight[i], value[i], count[i] = map(int, input().split())
dp = [[0]*(m+1) for _ in range(n+1)]

sol.main()