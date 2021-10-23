class Solution:
    def LCS(self, strX, strY, n, m):
        for i in range(1, n+1):
            for j in range(1, m+1):
                if strX[i-1] == strY[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
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
    
        return dp[n][m], result[::-1]
    
    def main(self, strX, strY):
        len_, str_ = self.LCS(strX, strY, len(strX), len(strY))
        print(len_)
        print(str_)

sol = Solution()
strX = input()
strY = input()
dp = [[0]*(len(strY) + 1) for _ in range(len(strX) + 1)]
sol.main(strX, strY)