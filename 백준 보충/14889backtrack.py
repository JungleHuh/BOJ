def dfs(team, idx):
    global min_diff
    if team == n//2:
        start,link = 0,0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        min_diff = min(min_diff, abs(start-link))
        return 

    for i in range(idx,n):
        if not visited[i] :
            visited[i] = 1
            dfs(team+1, i+1)
            visited[i] = 0

n = int(input())
visited = [0]* n
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0,0)
print(min_diff)