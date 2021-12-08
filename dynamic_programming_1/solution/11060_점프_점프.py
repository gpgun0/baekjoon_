n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [int(1e9)] * (n+1)
dp[1] = 0

for i in range(1, n+1):
    for j in range(1, nums[i]+1):
        if i + j <= n:
            dp[i+j] = min(dp[i]+1, dp[i+j])

if dp[-1] == int(1e9):
    print(-1)
else:
    print(dp[-1])
