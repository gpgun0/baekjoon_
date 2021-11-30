def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
parent = [i for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    union(parent, a, b)

for i in range(1, v+1):
    find_parent(parent, i)
print(parent.count(1) - 1)