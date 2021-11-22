import sys
sys.setrecursionlimit(10000)

def get_benefit(i, j, order):
  order += 1
  if j-i == 1:
    return max(v[i]*order + v[j]*(order+1), v[i]*(order+1) + v[j]*order)
  
  return max(get_benefit(i, j-1, order) + v[j]*order, get_benefit(i+1, j, order) + v[i]*order)

n = int(input())
v = [0] * n
for i in range(n):
  v[i] = int(input())

print(get_benefit(0, n-1, 0))