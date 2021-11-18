n = int(input())
works = [list(map(int, input().split())) for _ in range(n)]
works.sort(key=lambda x: x[1])
result = 1e9
total = 0
for t, l in works:
  total += t
  result = min(result, l - total)
  if result < 0:
    print(-1)
    exit()

print(result)