import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


M,N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(input()))
dx = [0,-1,0,1]
dy = [-1,0,1,0]
ans = 0
alpha = set()

def dfs(x,y,count):
    global ans
    ans = max(ans,count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and not graph[nx][ny] in alpha:
            alpha.add(graph[nx][ny])
            dfs(nx,ny,count+1)
            alpha.remove(graph[nx][ny])
alpha.add(graph[0][0])
dfs(0,0,1)
print(ans)