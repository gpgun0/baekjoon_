n = int(input())
eq = input()
d = {}
for i in range(65, 65+n):
  d[chr(i)] = int(input())
stack = []

for op in eq:
  
  if op == "+":
    stack.append(stack.pop() + stack.pop())
  elif op == "-":
    x = stack.pop()
    y = stack.pop()
    stack.append(y - x)
  elif op == "*":
    stack.append(stack.pop() * stack.pop())
  elif op == "/":
    x = stack.pop()
    y = stack.pop()
    stack.append(y / x)
  
  else:
    stack.append(d[op])

print("{:.2f}".format(stack[-1]))