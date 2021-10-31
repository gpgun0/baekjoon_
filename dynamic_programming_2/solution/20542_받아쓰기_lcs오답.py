class Solution:
    def main(self):
        n, m = map(int, input().split())
        ans1 = [0] + list(input())
        ans2 = [0] + list(input())
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if ans1[i] == ans2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                
                elif ans1[i] == 'i' and (ans2[j] == 'j' or ans2[j] == 'l'):
                    dp[i][j] = dp[i-1][j-1] + 1
                
                elif ans1[i] == 'v' and ans2[j] == 'w':
                    dp[i][j] = dp[i-1][j-1] + 1

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        lcs = dp[n][m]

        i, j = n, m
        while i >= 0 and j >= 0:
            if dp[i][j] == 1:
                str_ = ans1[i:i+lcs]
                if n >= m:
                    for k in range(i+1, n+1-lcs):
                        if str_ == ans1[k:k+lcs]:
                            return max(k, j) - 1 + max(n - (k + lcs - 1), m - (j + lcs - 1))
                else:
                    for k in range(j+1, m+1-lcs):
                        if str_ == ans1[k:k+lcs]:
                            return max(i, k) - 1 + max(n - (i + lcs - 1), m - (k + lcs - 1))

                return max(i, j) - 1 + max(n - (i + lcs - 1), m - (j + lcs - 1))
            if dp[i][j-1] == dp[i][j]:
                j -= 1
            elif dp[i-1][j] == dp[i][j]:
                i -= 1
            else:
                j -= 1
                i -= 1
        
        return max(n, m)
        
sol = Solution()
print(sol.main())