xy = [list(map(int, input().split())) for _ in range(int(input()))]

left_end = xy[0][0]
right_end = xy[0][1]
sum_ = 0
for x, y in xy[1:]:
  if right_end < x:
    sum_ += right_end - left_end
    left_end = x
  right_end = max(y, right_end)

sum_ += right_end - left_end
print(sum_)