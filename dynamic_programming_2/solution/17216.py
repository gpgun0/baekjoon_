class Solution:
    def main(self):
        dp = [num for num in arr]
        for i in range(2, n+1):
            for j in range(1, i):
                if arr[i] < arr[j]:
                    dp[i] = max(dp[i], arr[i] + dp[j])
        print(max(dp))

sol = Solution()
n = int(input())
arr = [0] + list(map(int, input().split()))
sol.main()