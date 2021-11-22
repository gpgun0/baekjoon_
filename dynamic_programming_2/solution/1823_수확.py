import sys
input = sys.stdin.readline

n = int(input())
v = [0] * n

for i in range(n):
  v[i] = int(input())

dp = [[0]*n for _ in range(n)]
for k in range(n):
  for i in range(n-k):
    j = i + k
    
    if i == j:
      dp[i][j] = v[i] * n
      continue

    dp[i][j] = max(dp[i][j-1] + v[j]*(n-k), dp[i+1][j] + v[i]*(n-k))

print(dp[0][-1])