class Solution:
    def main(self):
        n, k = map(int, input().split())
        dp = [1] + [0]*(k)

        for _ in range(n):
            cost = int(input())
            for x in range(cost, k+1):
                dp[x] = dp[x-cost] + dp[x]

        print(dp[-1])

sol = Solution()
sol.main()