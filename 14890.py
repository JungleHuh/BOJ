import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]


def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]