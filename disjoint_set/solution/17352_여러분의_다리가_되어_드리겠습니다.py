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

n = int(input())
parent = [i for i in range(n+1)]

for _ in range(n-2):
    a, b = map(int,input().split())
    union(a, b)

for i in range(1, n):
    for j in range(i+1, n+1):
        if find(i) != find(j):
            union(i, j)
            print(i, j)
            exit()