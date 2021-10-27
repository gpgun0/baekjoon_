class Solution:
    def main(self):
        a = input()

        if a == "1 2 3 4 5 6 7 8":
            return "ascending"
        elif a == "8 7 6 5 4 3 2 1":
            return "descending"
        else:
            return "mixed"



sol = Solution()
print(sol.main())