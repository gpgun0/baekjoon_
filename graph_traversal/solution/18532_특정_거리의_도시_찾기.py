from collections import *
import sys
input=sys.stdin.readline

def bfs(start):
    q = deque([start])
    dis[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dis[i] == -1:
                dis[i] = dis[now] + 1
                q.append(i)

    for i in range(2, n+1):
        if dis[i] == k:
            print(i)
    
    if not k in dis:
        print(-1)

n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
dis = [-1] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

bfs(x)