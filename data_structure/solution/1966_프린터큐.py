from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    l = [(i, p) for i, p in enumerate(list(map(int, input().split())))]
    q = deque(l)
    cnt = 0
    while True:
        x = q.popleft()

        if any(x[1] < y[1] for y in q):
            q.append(x)
        else:
            cnt += 1
            if x[0] == m:
                print(cnt)
                break