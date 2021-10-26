import sys
input = sys.stdin.readline
mod = 1000000009

class Solution:
  def main(self):
    n = int(input())

    if n < 4 or (dp[n][1] and dp[n][2] and dp[n][3]):
      return (dp[n][1] + dp[n][2] + dp[n][3] ) % mod

    for i in range(4, n+1):
      if dp[i][1] and dp[i][2] and dp[i][3]:
        continue
      dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % mod
      dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % mod
      dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % mod

    return (dp[n][1] + dp[n][2] + dp[n][3]) % mod


sol = Solution()
dp = [[0]*(4) for _ in range(100001)]
dp[1][1], dp[1][2], dp[1][3] = 1, 0, 0
dp[2][1], dp[2][2], dp[2][3] = 0, 1, 0
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1

t = int(input())
for _ in range(t):
  print(sol.main())