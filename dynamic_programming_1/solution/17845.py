class Solution:
    def main(self):
        n, k = map(int, input().split())
        dp = [[0]*(n+1) for _ in range(k+1)]
        value = [0]*(k+1)
        max_time = [0]*(k+1)

        for i in range(1, k+1):
            value[i], max_time[i] = map(int, input().split())

        for i in range(1, k+1):
            for j in range(1, n+1):
                if max_time[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-max_time[i]] + value[i])
        
        print(dp[k][-1])


sol = Solution()
sol.main()