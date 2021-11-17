tip = sorted([int(input()) for _ in range(int(input()))], reverse=True)

sum = 0

for i in range(len(tip)):
  sum += max(tip[i] - i, 0)

print(sum)
  