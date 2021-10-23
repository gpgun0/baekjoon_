import sys
input = sys.stdin.readline

class Solution:
    def main(self):
        n = int(input())
        game_board = [[0] + list(map(int, input().split())) + [0]*9 for _ in range(n)]
        game_board.insert(0, [0]*(n+10))
        for _ in range(9):
            game_board.append([0]*(n+10))
        
        dp = [[0]*(n+10) for _ in range(n+10)]
        dp[1][1] = 1

        for i in range(1, n+1):
            for j in range(1, n+1):
                if i==n and j==n:
                    print(dp)
                    return dp[n][n]
                if dp[i][j]:
                    dp[i+game_board[i][j]][j] += dp[i][j]
                    dp[i][j+game_board[i][j]] += dp[i][j]
                




sol = Solution()
print(sol.main())