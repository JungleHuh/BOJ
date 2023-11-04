from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        #i(노드 번호)는 이차원 그래프에 있는 인덱스를 의미해서
        #graph[v]라 함은 graph[0], graph[1], graph[2]를 의미한다    
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

