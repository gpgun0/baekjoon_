import sys
input = sys.stdin.readline
class Solution:
    def main(self):
        n = int(input())
        nums = [0]*n
        cnts = [0]*(10001)
        ans = [0]*n

        for i in range(n):
            nums[i] = int(input())
            cnts[nums[i]] += 1

        for i in range(1, 10001):
            cnts[i] = cnts[i] + cnts[i-1]
        
        for i in range(n-1, -1, -1):
            ans[cnts[nums[i]] - 1] = nums[i]
            cnts[nums[i]] -= 1
        
        print(*ans)

sol = Solution()
sol.main()