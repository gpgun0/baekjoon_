n = int(input())
dp = [0]*2 + [1]*(n-1)

for i in range(4, n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[-1])