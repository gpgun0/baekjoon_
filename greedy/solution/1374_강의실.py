import heapq as hq

n = int(input())
t = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

rooms = [0]
for i in range(n):
    et = rooms[0]
    if et <= t[i][1]:
        hq.heappop(rooms)

    hq.heappush(rooms, t[i][2])

print(len(rooms))