class Solution:
    def main(self):
        n = int(input())
        nums = list(map(int, input().split()))
        dp = [nums[0]] + [0]*(n-1)

        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i-1])

        return max(dp)        

sol = Solution()
for _ in range(int(input())): print(sol.main())