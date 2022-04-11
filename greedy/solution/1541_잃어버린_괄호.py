s = input().split("-")

result = sum(map(int, s[0].split("+")))

for i in range(1, len(s)):
    result -= sum(map(int, s[i].split("+")))

print(result)