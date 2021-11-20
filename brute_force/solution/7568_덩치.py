info = [list(map(int, input().split())) for _ in range(int(input()))]

for cur_w, cur_k in info:
    rank = 1
    for w, k in info:
        if cur_w < w and cur_k < k:
            rank += 1
    print(rank, end=" ")