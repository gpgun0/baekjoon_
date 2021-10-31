n, m = map(int, input().split()); l = n*m
while n % m: m, n = n % m, m
print(m, l//m)