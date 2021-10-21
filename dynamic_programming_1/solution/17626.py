INF = 1e9
class Solution:
    def main(self):
        n = int(input())

        dp = [INF]*(n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, n//2 + 1):
                if j*j > i:
                    break
                dp[i] = min(dp[i], dp[i-j*j] + 1)
        
        print(dp[-1])

sol = Solution()
sol.main()