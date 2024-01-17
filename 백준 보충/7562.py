import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, a, b, N):
    dx = [1, -1, -2, 2, -2, 2, -1, 1]
    dy = [-2, -2, -1, -1, 1, 1, 2, 2]

    queue = deque([(x, y, 0)])  # Starting position and initial step count as a tuple

    while queue:
        x, y, step = queue.popleft()

        if x == a and y == b:
            return step

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny, step + 1))

    return -1  # If the destination cannot be reached

# The number of test cases
T = int(input())

for _ in range(T):
    N = int(input())
    graph = [[0] * N for _ in range(N)]  # Fix initialization of the graph

    x, y = map(int, input().split())
    a, b = map(int, input().split())

    if x == a and y == b:
        print(0)
    else:
        result = bfs(x, y, a, b, N)
        print(result)
