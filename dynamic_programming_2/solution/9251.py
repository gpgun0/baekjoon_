import sys
sys.setrecursionlimit(100000)

class Solution:
    # def LCS(self, strX: str, strY: str, n: int, m: int):
    #     if dp[n][m] != -1:
    #         return dp[n][m]

    #     if n == -1 or m == -1:
    #         return 0

    #     if strX[n] == strY[m]:
    #         dp[n][m] = max(dp[n][m], 1 + self.LCS(strX, strY, n-1, m-1))
    #         return dp[n][m]
    #     else:
    #         dp[n][m] = max(self.LCS(strX, strY, n-1, m), self.LCS(strX, strY, n, m-1))
    #         return dp[n][m]

    def LCS(self, strX, strY, n, m):
        for i in range(1, n+1):
            for j in range(1, m+1):
                if strX[i-1] == strY[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        result = ""
        i = n
        j = m
        while dp[i][j] != 0:
            if dp[i][j] == dp[i][j-1]:
                j -= 1
            elif dp[i][j] == dp[i-1][j]:
                i -= 1

            else:
                result += strX[i-1]
                i -= 1
                j -= 1

        print(result[::-1])
        return dp[n][m]

    def main(self, strX: str, strY: str):
        return self.LCS(strX, strY, len(strX), len(strY))
        

sol = Solution()
strX = input()
strY = input()
dp = [[0]*(len(strY)+1) for _ in range(len(strX)+1)]
print(sol.main(strX, strY))
print(dp)