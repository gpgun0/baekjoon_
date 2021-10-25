class Solution:
    def main(self):
        r, c, w = map(int, input().split())
        dp = [[0]*(r+w) for _ in range(r+w)]
        
        for i in range(1, r+w):
            for j in range(1, i+1):
                if j == 0 or i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
        sum = 0
        for i in range(w):
            for j in range(i+1):
                sum += dp[i+r][j+c]
        return sum
        
sol = Solution()
print(sol.main())