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
        n = int(input())
        m = int(input())
        broken = [False]*10

        if m > 0:
            broken_nums = list(map(int, input().split()))
            for x in broken_nums:
                broken[x] = True
        
        min_ = 1e9
        for num in range(0, 1000001):
            if self.check(num, broken):
                min_ = min(min_, abs(n-num) + len(str(num)))

                
        return min(min_, abs(n-100))

sol = Solution()
print(sol.main())