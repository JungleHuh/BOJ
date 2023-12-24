import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
#상, 우, 하, 좌  (x는 밑으로 가는 방향, y는 옆(오른쪽)으로 가는 방향이라고 가정했을 때)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y,h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and ( 0 <= ny < N) and not visited[nx][ny] and zone[nx][ny] >h:
            visited[nx][ny] = True
            dfs(nx, ny, h)


N = int(input())
zone = [list(map(int, input().split())) for _ in range(N)]
ans = 1

for k in range(max(map(max, zone))):
    visited = [[False]* N for _ in range(N)]
    safe = 0
    for i in range(N):
        for j in range(N):
            if zone[i][j] > k and not visited[i][j]:
                safe += 1
                visited[i][j] = True
                dfs(i,j,k)
    ans = max(ans, safe)

print(ans)
