import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

for i in range(n):
    c = list(map(int, input().split()))
    
    for j in range(i+1, len(c)):
        if c[j] == 1:
            if find_parent(i+1) != find_parent(j+1):
                parent[find_parent(i+1)] = j+1

plan = list(map(int, input().split()))

prev = find_parent(plan[0])
for p in plan[1:]:
    if prev != find_parent(p):
        print("NO")
        break
else:
    print("YES")