import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    parent[max(a, b)] = min(a, b)

n, m = map(int,input().split())
parent = [i for i in range(n+1)]
pos = [[] for _ in range(n+1)]
graph = []
for i in range(1, n+1):
    x, y = map(int,input().split())
    pos[i] = (x, y)

for i in range(1, n):
    for j in range(i+1, n+1):
        x1, y1 = pos[i]
        x2, y2 = pos[j]
        dis = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        graph.append((dis, i, j))

graph.sort()

for _ in range(m):
    a, b = map(int,input().split())
    union(a, b)
result = 0
for e in graph:
    dis, a, b = e

    if find(a) != find(b):
        union(a, b)
        result += dis
print("{:.2f}".format(result))