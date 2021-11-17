n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))


for num in nums:
    l, r = 0, n-1
    while l <= r:
        mid = (l + r) // 2

        if card[mid] < num:
            l = mid + 1
        elif card[mid] > num:
            r = mid - 1
        else:
            print(1, end=" ")
            break
    else:
        print(0, end=" ")