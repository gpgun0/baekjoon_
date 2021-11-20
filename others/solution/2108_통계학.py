import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = [0] * n
for i in range(n):
    nums[i] = int(input())

nums.sort()

print(round(sum(nums) / n))
print(nums[n//2])
if n > 1 :
    comparison = Counter(nums).most_common()
    if comparison[0][1] == comparison[1][1]:
        print(comparison[1][0])
    else:
        print(comparison[0][0])

else: print(nums[0])
print(nums[-1] - nums[0])