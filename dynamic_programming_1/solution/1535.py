class Solution:
    def main(self):
        n = int(input())
        dp = [[0]*(100) for _ in range(n+1)]
        damage = [0] + list(map(int, input().split()))
        happiness = [0] + list(map(int, input().split()))

        for i in range(1, n+1):
            for j in range(1, 100):
                if damage[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-damage[i]] + happiness[i])
        
        print(dp[n][-1])
    
sol = Solution()
sol.main()