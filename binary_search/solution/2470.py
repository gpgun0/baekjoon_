class Solution:
    def main(self):
        n = int(input())
        solution = list(map(int, input().split()))
        left = 0
        right = n - 1

        solution.sort()

        min_ = 2000000001

        result = []

        while left < right:
            if min_ > abs(solution[left] + solution[right]):
                min_ = abs(solution[left] + solution[right])
                result = [solution[left], solution[right]]
            
            if abs(solution[left]) > abs(solution[right]):
                left += 1
            
            else:
                right -= 1
        
        return result

sol = Solution()
print(" ".join(map(str, sol.main())))