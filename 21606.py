from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def dfs(v, cnt):
    visited[v] = True

    for i in graph[v]:
        if location[i] == 1:
            cnt += 1
        elif not visited[i] and location[i] == 0:
            cnt = dfs(i, cnt)
    return cnt

ans = 0
n = int(stdin.readline())

location = [0] + list(map(int, stdin.readline().strip()))
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = list(map(int, stdin.readline().strip()))
    graph[a].append(b)
    graph[b].append(a)
    if location[a] == 1 and location[b] ==1:
        ans +=2

sum = 0
visited =  [False] * (n+1)
for i in range(1, n+1):
    if not visited[i] and location[i] == 0:
        x = dfs(i,0)
        sum += x*(x-1)

print(sum*ans)

