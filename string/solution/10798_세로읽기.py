arr = [[""]*15 for _ in range(5)]

for i in range(5):
    x = input()
    arr[i][:len(x)] = list(x)

result = ""

for i in range(15):
    for j in range(5):
        result += arr[j][i]

print(result)