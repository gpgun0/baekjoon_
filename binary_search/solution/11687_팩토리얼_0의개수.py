class Solution:
    def get_zero_num(self, num):
        result = 0

        x = 5
        while num >= x:
            result += (num // x)
            x = x * 5
        return result

    def main(self):
        m = int(input())

        l, h = 1, 100000000

        while l <= h:
            mid = (l + h) // 2
            
            result = self.get_zero_num(5*mid)
            if result < m:
                l = mid + 1
            elif result > m:
                h = mid - 1
            else:
                return 5*mid
        
        return -1
            


            

sol = Solution()
print(sol.main())