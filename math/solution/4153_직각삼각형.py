class Solution:
    def main(self):
        while True:
            x = list(map(int, input().split()))
            if x[0] == 0:
                break

            x.sort()

            if x[2] ** 2 == x[1] ** 2 + x[0] ** 2:
                print("right")
            else:
                print("wrong")
sol = Solution()
sol.main()