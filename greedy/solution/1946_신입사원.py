t = int(input())
for _ in range(t):
    n = int(input())
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort()

    cnt = 0
    cur_rank = 1e9
    for a, b in rank:
        if cur_rank > b:
            cnt += 1
            cur_rank = b
    
    print(cnt)