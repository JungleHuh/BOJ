N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
count = 0

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = 1
    global count
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            count += 1

dfs(1)
print(count)