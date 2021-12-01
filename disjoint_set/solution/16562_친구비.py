import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())

    if find_parent(a) != find_parent(b):
        parent[find_parent(a)] = b

for i in range(1, n+1):
    parent[i] = find_parent(i)
    
prev = -1
result = 0
for i in range(1, n+1):
    min_ = int(1e9)

    if prev != parent[i] and parent[i]:
        prev = parent[i]

        for j in range(i, n+1):
            if parent[j] == prev:
                min_ = min(min_, cost[j])
                parent[j] = 0
        result += min_

if result > k:
    print("Oh no")
else:
    print(result)