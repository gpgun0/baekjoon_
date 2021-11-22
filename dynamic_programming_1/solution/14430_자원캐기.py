n, m = map(int, input().split())
dp = [0]*n
for i in range(n):
    dp[i] = list(map(int, input().split()))
dp = [[0]*m] + dp

for i in range(1, n+1):
    for j in range(m):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        else:
            dp[i][j] = dp[i][j] + max(dp[i-1][j], dp[i][j-1])
    
print(dp[-1][-1])
