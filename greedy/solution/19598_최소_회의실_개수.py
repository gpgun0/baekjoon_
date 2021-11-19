import sys
import heapq as hq
input = sys.stdin.readline
t = [list(map(int, input().split())) for _ in range(int(input()))]
t.sort(key=lambda x: x[0])

rooms = [0]
cnt = 0

for s, e in t:
    if s >= rooms[0]:
        hq.heappop(rooms)
    else: 
        cnt += 1
    hq.heappush(rooms, e)


print(cnt)