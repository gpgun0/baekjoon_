class Solution:
    def main(self):
        a, b = [], []

        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
        for _ in range(2):
            x, y = map(int, input().split())
            
            if x in a:
                a.remove(x)
            else:
                a.append(x)
            
            if y in b:
                b.remove(y)
            else:
                b.append(y)
        
        print(a[0], b[0])

sol = Solution()
sol.main()