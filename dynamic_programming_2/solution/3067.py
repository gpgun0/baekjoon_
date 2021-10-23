class Solution:
    def main(self):
        n = int(input())
        coin_list = list(map(int, input().split()))
        m = int(input())
        dp = [1] + [0]*10000

        for cost in coin_list:
            for x in range(cost, m+1):
                dp[x] = dp[x-cost] + dp[x]

        return dp[m]

sol = Solution()
t = int(input())
for _ in range(t): print(sol.main())