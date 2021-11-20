n, k = map(int, input().split())
num = list(input())

stack = [num[0]]

for x in num[1:]:
    while stack and k and stack[-1] < x:
        stack.pop()
        k -= 1
    stack.append(x)

while k:
    stack.pop()
    k -= 1

print("".join(stack))