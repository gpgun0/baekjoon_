n = int(input())
a = b = 1

result = 1
for i in range(2, n+1):
    result = a % 15746 + b % 15746
    a, b = b % 15746, result % 15746

print(result % 15746)