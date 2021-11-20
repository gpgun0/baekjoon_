n = int(input())
desk = [[6, 6]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[1, 1] for _ in range(n+1)]

for i in range(1, n+1):
  for j in (0, 1):
    if desk[i][0] == desk[i-1][j]:
      dp[i][0] = max(dp[i][0], dp[i-1][j] + 1)
    
    if desk[i][1] == desk[i-1][j]:
      dp[i][1] = max(dp[i][1], dp[i-1][j] + 1)
      
max_ = -1
for i in range(1, n+1):
  for j in (0, 1):
    if dp[i][j] > max_:
      max_ = dp[i][j]
      grade = desk[i][j]

    if dp[i][j] == max_:
      grade = min(grade, desk[i][j])

print(max_, grade)