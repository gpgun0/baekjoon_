from collections import *
import sys
input=sys.stdin.readline

def bfs(start):
    q = deque([start])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not dis[i]:
                q.append(i)
                dis[i] = dis[now] + 1

    for i in range(1, n+1):
        if dis[i] == k:
            print(i)
    
    if not k in dis:
        print(-1)

n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
dis = [0] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

bfs(x)