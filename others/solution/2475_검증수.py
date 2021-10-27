class Solution:
    def main(self):
        return sum(map(lambda x: int(x)**2, input().split()))%10

sol = Solution()
print(sol.main())