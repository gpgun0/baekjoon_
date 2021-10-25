import sys
input = sys.stdin.readline

class Solution:
    def main(self):
        n, m = map(int, input().split())
        arr = [[0] + list(map(int, list(input().rstrip()))) for _ in range(n)]
        arr.insert(0, [0]*(m+1))
        
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        max_ = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if arr[i][j]:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    max_ = max(max_, dp[i][j])

        return max_ ** 2

sol = Solution()
print(sol.main())