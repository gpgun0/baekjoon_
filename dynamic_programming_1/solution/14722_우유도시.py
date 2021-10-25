import sys
input = sys.stdin.readline

class Solution:
    def main(self):
        n = int(input())
        milk_city = [[0] + list(map(int, input().split())) for _ in range(n)]
        milk_city.insert(0, [0]*(n+1))
        milk_city.append([0]*(n+1))

        dp = [[0]*(n+1) for _ in range(n+1)]


sol = Solution()
print(sol.main())