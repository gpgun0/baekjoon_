import heapq as hq
t = [list(map(int, input().split())) for _ in range(int(input()))]
t.sort(key = lambda x: x[0])
rooms = [0]
for s, e in t:
    et = rooms[0]
    if et <= s:
        hq.heappop(rooms)
    hq.heappush(rooms, e)
print(len(rooms))