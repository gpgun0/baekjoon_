n = int(input())

if n == 1 or n == 3:
    print(-1)
    exit()

cnt = 0
while n % 5 != 0:
    n -= 2
    cnt += 1

cnt += n // 5

print(cnt)