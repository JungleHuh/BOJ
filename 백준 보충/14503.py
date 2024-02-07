N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

def dfs(x,y):
    


