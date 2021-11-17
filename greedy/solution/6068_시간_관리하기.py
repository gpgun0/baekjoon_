n = int(input())
t = [[0]*2 for _ in range(n)]
for i in range(n):
  t[i][0], t[i][1] = map(int, input().split())

t.sort(key=lambda x: x[1])

result = t[0][1] - t[0][0]
if result < 0:
  print(-1)
  exit()

sum_ = 0
et = 0
for i in range(n):
  if i == 0:
    et = t[i][1]
  else:
    et = t[i][1] - t[i-1][1]
    
  if et - t[i][0] < 0:
    sum_ += et - t[i][0]
  else:
    sum_ += et - t[i][0]

  if sum_ < 0:
    print(-1)
    exit()

if result <= sum_:
  print(result)
else:
  print(sum_)