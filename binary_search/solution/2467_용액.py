class Solution:
    def main(self):
        n = int(input())
        s = list(map(int, input().split()))
        min_ = 2000000001

        l_, r_ = l, r = 0, n-1
        while  l < r:
            sum_ = s[l] + s[r]

            if min_ > abs(sum_):
                min_ = abs(sum_)
                l_, r_ = l, r

            if 0 > sum_:
                l += 1
            elif 0 < sum_:
                r -= 1
            else:
                print(s[l_], s[r_]) 
                return
        
        print(s[l_], s[r_])

sol = Solution()
sol.main()