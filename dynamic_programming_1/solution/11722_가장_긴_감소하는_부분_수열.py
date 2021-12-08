n = int(input())
nums = [0] + list(map(int, input().split()))

dp = [1]*(n+1)

for i in range(1, n):
    for j in range(i+1, n+1):
        if nums[i] > nums[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
