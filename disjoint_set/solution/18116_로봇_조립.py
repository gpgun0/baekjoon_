import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
        cnt[a] += cnt[b]
        cnt[b] = 0
    # else로 놔두면 a == b 일 때, 예외가 발생한다.
    # parent가 같은 경우엔 그냥 넘겨야 한다.
    elif a > b:
        parent[a] = b
        cnt[b] += cnt[a]
        cnt[a] = 0

n = int(input())
parent = [i for i in range(10**6 + 1)]
cnt = [1] * (10**6 + 1)

for _ in range(n):
    l = input()
    cmd = l.split()

    if cmd[0] == "I":
        union(int(cmd[1]), int(cmd[2]))
    else:
        print(cnt[find_parent(int(cmd[1]))])