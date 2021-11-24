n, m = map(int, input().split())
score = [[0]*m for _ in range(n)]

for i in range(n):
    score[i] = list(map(int, input().split()))

up = [[0]*m for _ in range(n)]
down = [[0]*m for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in range(m):
        if i == n-1 and j == 0:
            up[i][j] = score[i][j]
        elif i == n-1:
            up[i][j] = score[i][j] + up[i][j-1]
        elif j == 0:
            up[i][j] = score[i][j] + up[i+1][j]
        else:
            up[i][j] = score[i][j] + max(up[i][j-1], up[i+1][j])

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if i == n-1 and j == m-1:
            down[i][j] = score[i][j]
        elif i == n-1:
            down[i][j] = score[i][j] + down[i][j+1]
        elif j == m-1:
            down[i][j] = score[i][j] + down[i+1][j]
        else:
            down[i][j] = score[i][j] + max(down[i][j+1], down[i+1][j])

max_ = -1e9
for i in range(n):
    for j in range(m):
        max_ = max(max_, up[i][j] + down[i][j])

print(max_)