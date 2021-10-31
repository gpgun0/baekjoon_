class Solution:
    def main(self):
        n, k = map(int, input().split())
        coin = [0]*n

        for i in range(n):
            coin[i] = int(input())
            if coin[i] <= k:
                max_i = i
        
        cnt = 0
        for i in range(max_i, -1, -1):
            cnt = cnt + k // coin[i]
            k = k % coin[i]
        
        return cnt


sol = Solution()
print(sol.main())