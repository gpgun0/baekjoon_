n = int(input())
rgb = [[0]*n] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][j+1], dp[i-1][j+2])
        elif j == 1:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j+1])
        else:
            dp[i][j] = min(dp[i-1][j-2], dp[i-1][j-1])
        
        dp[i][j] += rgb[i][j]
        
print(min(dp[-1]))