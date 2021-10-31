class Solution:
    def main(self):
        n = int(input())
        time = list(map(int, input().split()))
        time.sort()
        dp = [time[0]] + [0]*(n-1)

        for i in range(1, n):
            dp[i] = time[i] + dp[i-1]

        return sum(dp)

sol = Solution()
print(sol.main())