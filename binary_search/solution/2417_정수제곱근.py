class Solution:
    def main(self):
        n = int(input())
        if n <= 2:
            return n
        
        r = 2
        i = 1
        while r <= n:
            i += 2
            r += i
        
        return (i-2)//2 + 2

sol = Solution()
print(sol.main())