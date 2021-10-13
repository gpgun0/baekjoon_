import sys
sys.setrecursionlimit(1000000)

class Solution:
    def fibonacci(self, n: int) -> int:
        if dp[n]:
            return dp[n]

        dp[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
        return dp[n] %  10007
    
    def main(self):
        return self.fibonacci(n)

    def main2(self):
        for i in range(3, n+1):
            dp[i] = dp[i-1] % 10007 + dp[i-2] % 10007
        return dp[n] % 10007

sol = Solution()
n = int(input())
dp = [0] * (n+2)
dp[1] = 1
dp[2] = 2
# print(sol.main())
print(sol.main2())