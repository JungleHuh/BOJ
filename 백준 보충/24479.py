import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]* (n+1)

cnt =1

def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt

    for i in graph[v]:
        if visited[i] == 0:
            cnt +=1
            dfs(graph, i, visited)


for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort(reverse=True)


dfs(graph, r, visited)

print(graph[1])


