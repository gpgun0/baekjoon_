n = int(input())

d = list(map(int, input().split()))
c = list(map(int, input().split()))

result = d[0] * c[0]

prev = c[0]
for i in range(1, n-1):
    cur = c[i]
    if prev <= cur:
        result += prev * d[i]
    else:
        result += cur * d[i]
        prev = cur

print(result)