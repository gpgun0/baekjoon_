import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    parent[max(a, b)] = min(a, b)

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)]
edges = []

for i in range(n):
    for j in range(i+1, n):
        if cost[i][j]:
            edges.append((cost[i][j], i, j))
edges.sort()

result = 0
for e in edges:
    c, a, b = e
    if find(a) != find(b):
        result += c
        union(a, b)

print(result)