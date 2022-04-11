triangleNumbers = [(i*(i+1))//2 for i in range(1, 51)]

def isPossible(x):
    for i in range(50):
        for j in range(50):
            for k in range(50):
                sum_ = triangleNumbers[i] + triangleNumbers[j] + triangleNumbers[k]
                if sum_ == x:
                    return 1
    
    return 0


for _ in range(int(input())):
    print(isPossible(int(input())))