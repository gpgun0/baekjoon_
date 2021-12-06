import sys
input=sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    parent[max(a, b)] = min(a, b)

n = int(input())

pos = [0]*n
edges = []
parent = [i for i in range(n)]
for i in range(n):
    x, y = map(float,input().split())
    pos[i] = (x, y)

for i in range(n-1):
    for j in range(i+1, n):
        x1, y1 = pos[i]
        x2, y2 = pos[j]
        dis = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
        edges.append((dis, i, j))

edges.sort()

result = 0
for e in edges:
    c, a, b = e
    if find(a) != find(b):
        result += c
        union(a, b)

print("{:.2f}".format(result))