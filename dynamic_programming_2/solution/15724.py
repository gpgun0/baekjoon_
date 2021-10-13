import sys
input = sys.stdin.readline

class Solution:
    def main(self):
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j] + sum(population[i][:j+1])
        
        k = int(input())

        for _ in range(k):
            x1, y1, x2, y2 = map(int, input().split())
            result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
            print(result)

sol = Solution()
n, m = map(int, input().split())
population = [[0] + list(map(int, input().split())) for _ in range(n)]
population.insert(0, [0]*(m+1))
dp = [[0]*(m+1) for _ in  range(n+1)]
sol.main()