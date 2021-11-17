roap = sorted([int(input()) for _ in range(int(input()))])
max_ = -1

for i in range(len(roap)):
    max_ = max(max_, roap[i] * (len(roap)-i))

print(max_)