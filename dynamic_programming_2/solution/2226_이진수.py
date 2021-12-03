n = int(input())
dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(i, 0, -1):
        dp[i] += dp[j]
    
    if i % 2 == 1:
        dp[i] += 1

print(dp[n-1])