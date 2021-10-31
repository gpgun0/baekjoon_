import sys
input = sys.stdin.readline

class Solution:
    def main(self):
        n, m = map(int, input().split())
        title = [input().split() for _ in range(n)]

        for _ in range(m):
            l, h = 0, len(title) - 1

            mob = int(input())
            while l <= h:
                mid = (l + h) // 2
                if mob <= int(title[mid][1]):
                    res = title[mid][0]
                    h = mid - 1
                else:
                    l = mid + 1
            
            print(res)

sol = Solution()
sol.main()