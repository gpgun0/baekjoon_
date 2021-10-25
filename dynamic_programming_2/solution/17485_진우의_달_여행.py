import sys
input = sys.stdin.readline

class Solution:
    def main(self):
        n, m = map(int, input().split())
        arr = [[1e9] + list(map(int, input().split())) + [1e9] for _ in range(n)]
        arr.insert(0, [0]*(m+1))
        dp = [[1e9]*(m+2) for _ in range(n)]
        dp.insert(0, [0]*(m+2))

        for i in range(1, n+1):
            for j in range(1, m+1):
                if i == 1:
                    dp[i][j] = arr[i][j]
                else:
                    dp[i][j] = min(min(arr[i-1][j-1], arr[i-1][j]) + dp[i-2][j-1],
                                    min(arr[i-1][j-1], arr[i-1][j+1]) + dp[i-2][j],
                                    min(arr[i-1][j], arr[i-1][j+1]) + dp[i-2][j+1]) + arr[i][j]
        
        print(dp)

sol = Solution()
sol.main()