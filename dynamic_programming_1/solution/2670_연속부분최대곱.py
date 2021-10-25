class Solution:
    def main(self):
        n = int(input())
        arr = [0]*(n+1)
        dp = [0]*(n+1)

        for i in range(1, n+1):
            arr[i] = float(input())

        for i in range(1, n+1):
            if i == 1:
                dp[i] = arr[i]
            else:
                dp[i] = max(arr[i], dp[i-1]*arr[i])
        
        return max(dp)


sol = Solution()
print("{:.3f}".format(sol.main()))