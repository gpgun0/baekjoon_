t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = sorted(list(map(int, input().split())))
    
    l, r = 0, n-1
    min_ = 1e9
    cnt = 0
    while l < r:
        diff = abs(k-(s[l]+s[r]))
        if diff == min_:
            cnt += 1
        elif diff < min_:
            cnt = 1
            min_ = diff
        
        if k >= s[l]+s[r]:
            l += 1
        elif k < s[l]+s[r]:
            r -= 1
    print(cnt)