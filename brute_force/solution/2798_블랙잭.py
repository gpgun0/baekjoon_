def sol():
    n, m = map(int, input().split())
    cards = sorted(list(map(int, input().split())))
    max_ = -1
    for p in range(n-1, 1, -1):
        l, r = 0, p - 1

        while l < r:
            sum_ = cards[l] + cards[r] + cards[p]

            if sum_ > m:
                r -= 1
            elif sum_ < m:
                max_ = max(max_, sum_)
                l += 1
            else:
                return sum_

    return max_

print(sol())