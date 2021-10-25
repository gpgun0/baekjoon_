class Solution:
    def main(self):
        n = int(input())
        dp = [0]*(n+2) # 중요
        t = [0]*(n+1)
        p = [0]*(n+1)

        for i in range(1, n+1):
            t[i], p[i] = map(int, input().split())
        
        max_ = 0
        for i in range(1, n+1):
            max_ = max(max_, dp[i]) # 순서 중요 if문 뒤
            if i + t[i] > n + 1:
                continue

            dp[i+t[i]] = max(max_ + p[i], dp[i+t[i]])

        return max(dp)

sol = Solution()
print(sol.main())