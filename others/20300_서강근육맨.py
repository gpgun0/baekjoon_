n = int(input())
loss = list(map(int, input().split()))
loss.sort()
if n % 2 == 0:
    max_ = 0
    for i in range(n//2):
        max_ = max(max_, loss[i] + loss[n-i-1])
else:
    max_ = loss[-1]
    for i in range(n//2):
        max_ = max(max_, loss[i] + loss[n-i-2])

print(max_)