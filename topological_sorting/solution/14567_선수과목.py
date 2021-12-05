from collections import deque
import copy
import sys
input=sys.stdin.readline

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
semester = [1]*(n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = copy.deepcopy(semester)
    q = deque()

    for i in range(n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + 1)
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i], end=" ")

topology_sort()