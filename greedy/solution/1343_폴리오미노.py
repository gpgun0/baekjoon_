b = input()

cnt = 0
result = ""
for x in b:
    if x == ".":
        if cnt % 2 != 0:
            print(-1)
            exit()
        else:
            if cnt % 4 == 0:
                result += "AAAA" * (cnt//4) + "."
            else:
                result += "AAAA" * (cnt//4) + "BB" + "."
        cnt = 0
    else:
        cnt += 1

if cnt:
    if cnt % 2 != 0:
        print(-1)
        exit()
    else:
        if cnt % 4 == 0:
            result += "AAAA" * (cnt//4)
        else:
            result += "AAAA" * (cnt//4) + "BB"

print(result)