n, k = map(int, input().split())

q = [i for i in range(1, n+1)]

i = 0
result = "<"
while len(q) != 1:
    i += k - 1
    i %= len(q)
    result += str(q.pop(i)) +", "
    

print(result + str(q[0]) + ">")