class Solution:
    def main(self):
        n = int(input())
        sols = sorted(list(map(int, input().split())))

        min_ = 999999998+999999999+1000000000
        p_, l_, r_ = n-1, 0, n-2

        for p in range(n-1, 1, -1):
            l, r = 0, p-1
            
            while l < r:
                sum_ = sols[p] + sols[l] + sols[r]

                if min_ >= abs(sum_):
                    min_ = abs(sum_)
                    p_, l_, r_ = p, l, r

                if 0 > sum_:
                    l += 1
                elif 0 < sum_:
                    r -= 1
                else:
                    print(sols[l_],sols[r_], sols[p_])
                    return 
        
        print(sols[l_],sols[r_], sols[p_])


sol = Solution()
sol.main()