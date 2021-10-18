class Solution:
    def combination(self, m, n):
        if dp[m][n]:
            return dp[m][n]

        if m <= n: 
            dp[m][n] = 1
            return dp[m][n]
        
        if n == 1:
            dp[m][n] = m
            return dp[m][n]
        
        dp[m][n] = self.combination(m-1, n-1) + self.combination(m-1, n)
        return dp[m][n]


    def main(self):
        n, m = map(int, input().split())
        return self.combination(m, n)


sol = Solution()
t = int(input())
dp = [[0]*201 for _ in range(201)]
for _ in range(t): print(sol.main())