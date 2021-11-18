n = int(input())
d = sorted(list(map(int, input().split())))
print(sum([x / 2 for x in d[:n-1]]) + max(d))