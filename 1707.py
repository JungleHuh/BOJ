from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
    q = deque()
    visited[start] = end
    q.append(start)

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] * -1
                q.append(i)

            elif visited[i] == visited[v]:
                return False
    return True
    
t = int(input())

for _ in range(t):
    u,v = map(int, input().split())
    graph = [[] for _ in range(u+1)]
    visited = [0] * (u+1)


    for _ in range(v):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    for i in range(1, u+1):
        if not visited[i]:
            result = bfs(i,1)
            if not result:
                break

    if result:
        print("YES")
    else:
        print("NO")





