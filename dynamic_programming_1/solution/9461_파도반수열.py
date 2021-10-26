class Solution:
  def main(self):
    n = int(input())
    
    if n < 5 or dp[n]:
      return dp[n]

    for i in range(5, n+1):
      if dp[i]:
        continue
      
      dp[i] = dp[i-1] + dp[i-5]

    return dp[n]
      

sol = Solution()
t = int(input())
dp = [0]*(101)
dp[1] = dp[2] = dp[3] = 1
dp[4] = 2
for _ in range(t):
  print(sol.main())