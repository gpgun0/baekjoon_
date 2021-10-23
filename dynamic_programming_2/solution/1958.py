class Solution:
    def LCS(self, strX: str, strY: str, strZ: str, n: int, m: int, l: int):
        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(1, l+1):
                    if strX[i-1] == strY[j-1] and strX[i-1] == strZ[k-1]:
                        dp[i][j][k] = 1 + dp[i-1][j-1][k-1]
                    else:
                        dp[i][j][k] = max(max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1]), \
                            max(dp[i-1][j-1][k], dp[i-1][j][k-1], dp[i][j-1][k-1]))

        return dp[n][m][l]

    def main(self, strX: str, strY: str, strZ: str):
        return self.LCS(strX, strY, strZ, len(strX), len(strY), len(strZ))
        
sol = Solution()
strX = input()
strY = input()
strZ = input()
dp = [[[0]*(len(strZ) + 1) for _ in range(len(strY) + 1)] for _ in range(len(strX) + 1)]
print(sol.main(strX, strY, strZ))