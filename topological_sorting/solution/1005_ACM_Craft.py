from collections import deque
import copy
import sys
input=sys.stdin.readline

def topology_sort():
    ith = int(input())

    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(result[ith])

for _ in range(int(input())):
    n, k = map(int, input().split())

    graph = [[] for i in range(n+1)]
    indegree = [0] * (n+1)
    time = [0] + list(map(int, input().split()))

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    topology_sort()