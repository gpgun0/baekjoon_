n = int(input())
l = input()
sum_ = 0
for i in range(n):
    sum_ += (ord(l[i]) - 96) * 31 ** i
print(sum_ % 1234567891)