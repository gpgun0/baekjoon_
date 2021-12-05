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

v = int(input())
e = int(input())

parent = [i for i in range(v+1)]
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

result = 0
for e in edges:
    c, a, b = e
    if find(a) != find(b):
        result += c
        union(a, b)

print(result)