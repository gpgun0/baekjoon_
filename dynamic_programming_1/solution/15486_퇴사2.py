import sys

class Solution:
  def main(self):
    input = sys.stdin.readline

    n = int(input())
    dp = [0] * (n+2)
    t = [0] * (n+1)
    p = [0] * (n+1)

    for i in range(1, n+1):
      t[i], p[i] = map(int, input().split())
    
    max_ = 0
    for i in range(1, n+1):
      max_ = max(max_, dp[i])
      
      if i + t[i] > n+1:
        continue

      dp[i+t[i]] = max(p[i] + max_, dp[i+t[i]])

    # for i in range(n, 0, -1):
    #   t[i], p[i] = map(int, input().split())
    
    # max_ = 0
    # for i in range(1, n+1):

    #   if i - t[i] < 0:
    #     continue
    #   # max_ = max(dp[:i-t[i]+1])

    #   dp[i] = max(p[i] + dp[i-t[i]], max_)
    #   max_ = max(max_, dp[i])

    # print(dp)
    return max(dp)

sol = Solution()
print(sol.main())