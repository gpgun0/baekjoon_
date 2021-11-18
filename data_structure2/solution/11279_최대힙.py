import sys
import heapq as hq
input = sys.stdin.readline

a = []
for _ in range(int(input())):
    x = int(input())

    if x == 0:
        if not a:
            print(0)
        else:
            print(-hq.heappop(a))
    
    else:
        hq.heappush(a, -x)
