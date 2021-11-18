p = sorted([int(input()) for _ in range(int(input()))], reverse=True)

sum_ = 0
for i in range(len(p)):
    if i % 3 == 2:
        continue
    sum_ += p[i]

print(sum_)