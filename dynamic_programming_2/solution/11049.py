INF = int(22e8)

class Solution:
    def matrix_chain(self, i: int, j: int):
        if i >= j:
            return 0

        if dp[i][j] != INF:
            return dp[i][j]
        
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], self.matrix_chain(i, k) + self.matrix_chain(k+1, j) + arr[i-1]*arr[k]*arr[j])

        return dp[i][j]

    def main(self):
        i = 1
        j = n

        for k in range(i, j):
            dp[i][j] = min(dp[i][j], self.matrix_chain(i, k) + self.matrix_chain(k+1, j)  + arr[i-1]*arr[k]*arr[j])
         
        return dp[i][j]

sol = Solution()
n = int(input())
arr = []
for _ in range(n):
    row_of_matrix, col_of_matrix = map(int, input().split())
    arr.append(row_of_matrix)
arr.append(col_of_matrix)
dp = [[INF]*(n+1) for _ in range(n+1)]
print(sol.main())