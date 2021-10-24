class Solution:
  def main(self):
    n = int(input())
    arr = [0]*(n+2)
    dp = [0]*(n+2)

    for i in range(1, n+1):
      arr[i] = int(input())
    
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    
    if n <= 2:
      return dp[n]
    for i in range(3, n+1):
      dp[i] = max(dp[i-2], dp[i-3] + arr[i-1], dp[i-4] + arr[i-1]) + arr[i]
    
    return max(dp)

      

sol = Solution()
print(sol.main())