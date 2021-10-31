class Solution:
    def main(self):
        n, m = map(int, input().split())
        ans1 = [0] + list(input())
        ans2 = [0] + list(input())
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)

                elif ans1[i] == ans2[j] or \
                    (ans1[i] == 'i' and (ans2[j] == 'j' or ans2[j] == 'l')) or \
                    (ans1[i] == 'v' and ans2[j] == 'w'):
                    dp[i][j] = dp[i-1][j-1]
                
                elif ans1[i] != ans2[j]:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1

        return dp[n][m]
sol = Solution()
print(sol.main())