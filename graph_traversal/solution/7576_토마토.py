from collections import *
import sys
input=sys.stdin.readline

def bfs():
    q = deque()
    day = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i, j))
    
    while q:
        cur_x, cur_y = q.popleft()

        for x, y in dirs:
            x += cur_x
            y += cur_y

            if x <= -1 or x >= n or y <= -1 or y >= m \
                or arr[x][y] == -1:
                continue
            elif arr[x][y] == 0: # 이 조건 때문에 max, min 고려할 필요 없다.
                arr[x][y] = arr[cur_x][cur_y] + 1
                q.append((x, y))

m, n = map(int,input().split())
arr = [0]*n
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

bfs()
result = 0
for i in arr:
    if not all(i):
        print(-1)
        exit()
    result = max(result, max(i))
print(result-1)