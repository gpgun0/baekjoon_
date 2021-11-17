n = int(input())

s1 = []
s2 = [0] * n

result = ""
for i in range(n-1, -1, -1):
    s2[i] = int(input())

i = 1
while i <= n:
    if not s1:
        s1.append(i)
        i += 1
        result += "+"
        continue

    if s1[-1] != s2[-1]:
        s1.append(i)
        i += 1
        result += "+"
    else:
        s1.pop()
        s2.pop()
        result += "-"
    
while s1:
    if s1[-1] == s2[-1]:
        s1.pop()
        s2.pop()
        result += "-"
    else:
        result = "NO"
        break

if result == "NO":
    print(result)
else:
    for s in result:
        print(s)