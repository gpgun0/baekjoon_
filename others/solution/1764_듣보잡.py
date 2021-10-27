class Solution:
    def main(self):
        n, m = map(int, input().split())
        a = [input() for _ in range(n)]
        b = [input() for _ in range(m)]
        
        result = list(set(a) & set(b))
        print(len(result))
        for name in sorted(result):
            print(name)
        

sol = Solution()
sol.main()