from collections import *
import sys
input=sys.stdin.readline

dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(start):
    q = deque([start])

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            new_x, new_y = x+dx, y+dy
            if 0 <= new_x <= n-1 and 0 <= new_y <= m-1 and\
                arr[new_x][new_y] == 1 and (new_x != 0 or new_y != 0):

                arr[new_x][new_y] = arr[x][y] + 1
                q.append((new_x, new_y))

n, m = map(int,input().split())

arr = [[] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().rstrip()))

bfs((0, 0))

print(arr[-1][-1])