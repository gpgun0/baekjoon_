t = int(input())
k = int(input())

dp = [[1] + [0]*(t) for _ in range(k+1)]

coin = [[0]*2 for _ in range(k+1)]

for i in range(1, k+1):
    coin[i][0], coin[i][1] = map(int, input().split())

coin.sort()


for i in range(1, k+1):
    for j in range(1, t+1):
        if coin[i][0] > j:
            dp[i][j] = dp[i-1][j]
            continue

        for k in range(1, coin[i][1] + 1):
            if j - k*coin[i][0] >= 0:
                dp[i][j] += dp[i-1][j-k*coin[i][0]]

        dp[i][j] += dp[i-1][j]
        
# print(dp)
print(dp[-1][-1])