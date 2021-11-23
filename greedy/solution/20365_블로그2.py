n = int(input())
color = input()

prev = ""
b_cnt = 0
r_cnt = 0
for c in color:
    if prev != c:
        if c == "B":
            b_cnt += 1
        else:
            r_cnt += 1
        prev = c

print(min(b_cnt + r_cnt, 1 + min(b_cnt, r_cnt)))