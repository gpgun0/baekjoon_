import sys
input = sys.stdin.readline

while True:
    l = input().strip()
    if not l:
        break

    s, t = l.split()
    si = 0
    for ti in range(len(t)):
        if t[ti] == s[si]:
            si += 1
            if si == len(s):
                print("Yes")
                break
    else:
        print("No")