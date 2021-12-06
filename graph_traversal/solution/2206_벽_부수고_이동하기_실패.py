from collections import *
import sys
input=sys.stdin.readline

def bfs():
    q = deque([(0, 0)])
    graph[0][0] = 1
    check[0][0] = "l" 

    q.append((n-1, m-1))
    graph[n-1][m-1] = 1
    check[n-1][m-1] = "r"
    
    result = int(1e9)
    while q:
        cur_x, cur_y = q.popleft()
        for x, y in dirs:
            x += cur_x
            y += cur_y

            if x <= -1 or x >= n or y <= -1 or y >= m:
                continue
            elif graph[x][y] == 0:
                graph[x][y] = graph[cur_x][cur_y] + 1
                q.append((x, y))
                check[x][y] = check[cur_x][cur_y]

    for i in range(n):
        for j in range(m):
            if check[i][j] == "":

                if i != 0 and i != n-1:
                    if check[i-1][j] == "l" and check[i+1][j] == "r":
                        result = min(result, 1 + graph[i-1][j] + graph[i+1][j])
                    
                if j != 0 and i != n-1:
                    if check[i][j-1] == "l" and check[i+1][j] == "r":
                        result = min(result, 1 + graph[i][j-1] + graph[i+1][j])

                if j != 0 and j != m-1:
                    if check[i][j-1] == "l" and check[i][j+1] == "r":
                        result = min(result, 1 + graph[i][j-1] + graph[i][j+1])

                if i != 0 and j != m-1:
                    if check[i-1][j] == "l" and check[i][j+1] == "r":
                        result = min(result, 1 + graph[i-1][j] + graph[i][j+1])
                
                if i != 0 and j != 0:
                    if check[i-1][j] == "r" and check[i][j-1] == "l":
                            result = min(result, 1 + graph[i-1][j] + graph[i][j-1])
                    
                if i != n-1 and j != m-1:
                    if check[i+1][j] == "l" and check[i][j+1] == "r":
                            result = min(result, 1 + graph[i+1][j] + graph[i][j+1])
                    

            if check[i][j] == "l":
                if j != m-1 and check[i][j+1] == "r":
                    result = min(result, graph[i][j] + graph[i][j+1])
                if i != n-1 and check[i+1][j] == "r":
                    result = min(result, graph[i+1][j] + graph[i][j])
    if n == 1 and m == 1:
        print(1)
        exit()

    if result == int(1e9):
        print(-1)
    else:
        print(result)
    
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int,input().split())
graph = [[] for _ in range(n)]

check = [[""]*m for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().rstrip()))

bfs()
