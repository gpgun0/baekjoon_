import sys
input = sys.stdin.readline

class Solution:
  def main(self):
    n = int(input())
    nums = [0] + list(map(int, input().split()))

    dp = [[0]*(n+1) for _ in range(n+1)]

    for s in range(1, n):
      for i in range(1, n+1-s):
        j = i+s

        if nums[i] == nums[j]:
          if dp[i+1][j-1] == 0:
            dp[i][j] = 0
          else:
            dp[i][j] = dp[i+1][j-1]
          continue
      
        dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    
    return dp[1][-1]

sol = Solution()
print(sol.main())