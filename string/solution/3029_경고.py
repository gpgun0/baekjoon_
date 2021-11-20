cur = list(map(int, input().split(":")))
dead = list(map(int, input().split(":")))

if cur == dead:
    print("24:00:00")
    exit()

if cur[2] > dead[2]: dead[1] -= 1
if cur[1] > dead[1]: dead[0] -= 1

ss = (dead[2] - cur[2]) % 60
mm = (dead[1] - cur[1]) % 60
hh = (dead[0] - cur[0]) % 24

print("{0:02d}:{1:02d}:{2:02d}".format(hh, mm, ss))