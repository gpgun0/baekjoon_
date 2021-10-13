class Solution:
    def main(self):
        for i in range(3, n+1):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker_list[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker_list[1][i]
        
        return max(dp[0][-1], dp[1][-1])

sol = Solution()

t = int(input())
for _ in range(t):
    n = int(input())
    sticker_list = [[0] + list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*(n+1) for _ in range(2)]
    
    dp[0][1] = sticker_list[0][1]
    dp[1][1] = sticker_list[1][1]

    if n >= 2:
        dp[0][2] = dp[1][1] + sticker_list[0][2]
        dp[1][2] = dp[0][1] + sticker_list[1][2]

    print(sol.main())