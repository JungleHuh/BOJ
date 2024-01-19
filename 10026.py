import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
visited = [[0]*n for _ in range(n)]
sum1 = 0
sum2 = 0
graph = []
for _ in range(n):
    graph.append(list(input()))

def dfs(x,y,color):
    visited[x][y] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0<= ny <n and visited[nx][ny] == 0:
            if graph[nx][ny] == color:
                dfs(nx,ny,color)

for color in ['R','G','B']:
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i,j,color)
                sum1 +=1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
        

visited = [[0]*n for _ in range(n)]

for color in ['R','B']:
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j,color)
                sum2 += 1

print(sum1, sum2)