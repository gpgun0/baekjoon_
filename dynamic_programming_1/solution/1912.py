class Solution:
    def main(self):
        for i in range(1, n+1):
            dp[i] = max(arr[i], dp[i-1] + arr[i])
        
        return max(dp[1:])


sol = Solution()
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [0] * (n+1)
dp[1] = arr[1]
print(sol.main())