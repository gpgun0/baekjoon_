from collections import Counter

for i in range(int(input())):
    x = Counter(input().replace(" ", "")).most_common()

    if len(x) == 1:
        print(x[0][0])
        continue
    
    if x[0][1] == x[1][1]:
        print("?")
    else:
        print(x[0][0])