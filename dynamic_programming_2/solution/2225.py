class Solution:
    def main(self, n, k):
        if dp[n][k]:
            return dp[n][k]

        if k == 1:
            dp[n][k] == 1
            return dp[n][k]
        self.main(n - 1)
        

sol = Solution()
n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
sol.main(n, k)