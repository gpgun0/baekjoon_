n, k = map(int, input().split())
children = list(map(int, input().split()))
diff = [0] * (n-1)

x = children[0]
for i in range(1, len(children)):
  diff[i-1] = children[i] - x
  x = children[i]

diff.sort()
print(sum(diff[:n-k]))