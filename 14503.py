dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y,dir):
    global ans
    if graph[x][y] == 0:
        graph[x][y] = 2
        ans += 1
    for _ in range(4):
        nd = (dir + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if graph[nx][ny] == 0:
            dfs(nx,ny,nd)
            return
        dir = nd
    nd = (dir+ 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if graph[nx][ny] == 1:
        return
    dfs(nx,ny,dir)

N,M = map(int, input().split())
x,y, dir = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dfs(x,y,dir)
print(ans)



    