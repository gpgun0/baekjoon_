n = int(input())
dp = [i // 2 for i in range(1, n+2)]

for c in [5, 7]:
  for i in range(1, n+1):
    if c <= i:
      dp[i] = min(dp[i], dp[i-c] + 1)

print(dp[-1])