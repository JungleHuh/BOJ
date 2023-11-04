from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [[]for _ in range(N+1)]
inDegree = [0]* (N+1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1
    
q = deque()
ans = []

for s in range(1, N+1):
    if inDegree[s] == 0:
        q.append(s)
while q:
    s = q.popleft()
    ans.append(s)
    
    for adj_s in graph[s]:
        inDegree[adj_s] -= 1
        if inDegree[adj_s] ==0:
            q.append(adj_s)
            
print(*ans, sep=" ")
    
