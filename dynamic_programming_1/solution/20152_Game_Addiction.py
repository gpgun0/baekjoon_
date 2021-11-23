h, n = map(int, input().split())
l = abs(h-n) + 1
dp = [[0]*l for _ in range(l)]
dp[0][0] = 1

for i in range(1, l):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1])