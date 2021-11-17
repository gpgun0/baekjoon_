class Solution:
    def myself(self):
        s = int(input())
        dp = [0] + [i for i  in range(1, 100001)]
        for i in range(1, 100001):
            dp[i] = dp[i] + dp[i-1]
        
        l, r = 1, 100000
        
        while l <= r:
            mid = (l + r) // 2

            if dp[mid] <= s:
                res = mid
                l = mid + 1
            
            elif dp[mid] > s:
                r = mid - 1

        return res

    def main(self):
        s = int(input())

        n = 0
        i = 1
        while n <= s:
            n += i
            i += 1

        return i-2

sol = Solution()
print(sol.main())

from math import *
print(floor(sqrt(2*int(input())+1/4)-0.5))