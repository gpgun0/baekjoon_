import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    parent[max(a, b)] = min(a, b)

n, m = map(int, input().split())


parent = [i for i in range(n+1)]
edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

result = 0
cnt = 0
for e in edges:
    cost, a, b = e
    if find(a) != find(b) and cnt < n - 2:
        result += cost
        union(a, b)
        cnt += 1
    
print(result)