import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


n, m = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(m):
    o, a, b = map(int, input().split())

    if o == 1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")

    else:
        if find_parent(a) != find_parent(b):
            parent[find_parent(a)] = b