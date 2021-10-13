class Solution:
    def main(self):
        n = int(input())
        coin_list = list(map(int, input().split()))
        m = int(input())
        dp = [1]+[0]*(m)

        for coin in coin_list:
            for i in range(coin, m+1):
                # dp[i]: 이번 coin을 안쓰고 만들 수 있는 경우의 수
                # dp[i-coin]: (현재 돈) - (현재 coin)원 을 현재 coin을 쓰고 만들 수 있는 경우의 수 
                dp[i] = dp[i] + dp[i-coin]

        print(dp[-1])


sol = Solution()
t = int(input())
for _ in range(t):
    sol.main()