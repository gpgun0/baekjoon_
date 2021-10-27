# print(*sorted(eval("input(),"*int(input()))))

def merge_sort(nums):
    if len(nums) > 1:

        mid = len(nums) // 2

        L = nums[:mid]
        R = nums[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[i+j] = L[i]
                i += 1
            else:
                nums[i+j] = R[j]
                j += 1

        
        if i < len(L):
            nums[i+j:] = L[i:]
        elif j < len(R):
            nums[i+j:] = R[j:]

n = int(input())
nums = [int(input()) for _ in range(n)]
merge_sort(nums)
list(map(print, nums))