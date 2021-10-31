class Solution:
    def check(self, num, broken):
        if num == 0:
            if broken[num]:
                return False

        while num:
            if broken[num % 10]:
                return False
            num = num // 10
        
        return True

    def main(self):
        n_down = n_up = n = int(input())
        m = int(input())
        broken = [False]*10


        if m > 0:
            broken_nums = list(map(int, input().split()))
            for x in broken_nums:
                broken[x] = True
        
        if m == 10:
            return abs(n - 100)
            
        cnt1 = 0
        while True:
            if n_down == -1:
                cnt1 = 1e9
                break
            if not self.check(n_down, broken):
                n_down -= 1
                cnt1 += 1
                continue
            else:
                break

        cnt2 = 0
        while True:
            if cnt2 > cnt1:
                cnt2 = 1e9
                break
            if not self.check(n_up, broken):
                n_up += 1
                cnt2 += 1
                continue
            else:
                break
        

        if cnt1 < cnt2:
            result = cnt1 + len(str(n_down))
        elif cnt1 > cnt2:
            result = cnt2 + len(str(n_up))
        else:
            result = cnt1 + min(len(str(n_down)), len(str(n_up)))

        return min(result, abs(n-100))

sol = Solution()
print(sol.main())