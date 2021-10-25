import sys
input = sys.stdin.readline

class Solution:
    def main(self):
        n, m = map(int, input().split())
        arr = [[0] + list(map(int, input().split())) for _ in range(n)]
        arr.insert(0, [0]*(n+1))
        
        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + sum(arr[i][:j+1])
        
        for _ in range(m):
            x1, y1, x2, y2 = map(int, input().split())
            print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])


sol = Solution()
sol.main()