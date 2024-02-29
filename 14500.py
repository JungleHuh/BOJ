import sys
input = sys.stdin.readline


N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
maximum = 0

def dfs(x,y,temp, count):
    global maximum
    if count == 4:
        maximum = max(maximum, temp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M or visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        dfs(nx,ny,temp+ graph[nx][ny],count+1)
        visited[nx][ny] = 0

def dfs_last(x,y):
    global maximum
    temp = graph[x][y]
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M or visited[nx][ny]:
            continue
        arr.append(graph[nx][ny])
    length = len(arr)
    if length == 4:
        arr.sort(reverse= True)
        arr.pop()
        maximum = max(maximum, sum(arr)+ graph[x][y])
    elif length == 3:
        maximum = max(maximum, sum(arr)+ graph[x][y])
        return

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i,j,graph[i][j], 1)
        dfs_last(i,j)
        visited[i][j] = 0
print(maximum)