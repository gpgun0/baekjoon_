n = int(input())

cnt = 0
x = 666
while True:
    if "666" in str(x):
        cnt += 1
    
    if cnt == n:
        break
    x += 1
print(x)