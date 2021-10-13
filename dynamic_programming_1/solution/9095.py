class Solution:
    def recurrenceRelation(self, n: int) -> int:
        if dp[n]:
            return dp[n]

        dp[n] = self.recurrenceRelation(n-1) + self.recurrenceRelation(n-2) + self.recurrenceRelation(n-3)
        return dp[n]

    def main(self, t: int):
        for _ in range(t):
            n = int(input())
            print(self.recurrenceRelation(n))
        

sol = Solution()
t = int(input())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
sol.main(t)