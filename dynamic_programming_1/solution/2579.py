class Solution:
    def main(self):
        dp[1] = arr[1]
        dp[2] = arr[1] + arr[2]

        if n == 1 or n == 2:
            return dp[n]

        for i in range(3, n+1):
            dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
        
        return dp[n]


sol = Solution()
n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
arr.append(0)
dp = [0] * (n+2)
print(sol.main())