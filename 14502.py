import sys
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    global ans
    if graph[x][y] == 0:
        graph[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

