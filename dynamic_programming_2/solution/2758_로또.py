class Solution:
    def main(self):
        n, m = map(int, input().split())

        for i in range(1, n+1):
            for j in range(2**(i-1), m+1):
                if j == 2 ** (i-1):
                    dp[i][j] = 1
                    continue

                dp[i][j] = dp[i][j-1] + dp[i-1][j//2]

        return dp[n][m]
        

sol = Solution()
dp = [[0]*2001 for _ in range(11)]
dp[0] = [1]*2001
t = int(input())
for _ in range(t):
    print(sol.main())