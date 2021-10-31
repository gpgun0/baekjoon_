class Solution:
    def main(self):
        n, k = map(int, input().split())
        
        p = n + 2
        l, h = 1, (n+2)//2
        
        while l <= h:
            mid = (l + h) // 2

            result = mid * (p - mid)

            if result < k:
                l = mid + 1
            elif result > k:
                h = mid - 1
            else:
                return "YES"
        
        return "NO"
            
sol = Solution()
print(sol.main())