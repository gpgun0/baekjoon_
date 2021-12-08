n = int(input())
nums = [0] + list(map(int, input().split()))

dp1 = [1]*(n+1)
dp2 = [1]*(n+1)

for i in range(2, n+1):
    if nums[i] >= nums[i-1]:
        dp1[i] = dp1[i-1] + 1
    if nums[i] <= nums[i-1]:
        dp2[i] = dp2[i-1] + 1

print(max(max(dp1), max(dp2)))