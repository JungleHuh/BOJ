from collections import deque
import sys

input = sys.stdin.readline
#보드의 크기
n = int(input())
#사과의 위치: 1
k = int(input())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)] 

for i in range(k):
    a,b = map(int, input().split())
    graph[a][b] = 1

curve_num = int(input())
curve = []
for _ in range(curve_num):
    time,lr = input().split()
    curve.append((int(time), lr))


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, lr):
    if lr == "L":
        direction = (direction -1)%4
    elif lr == "D":
        direction = (direction +1)%4
    return direction

queue = deque()

def simulate():
    x,y = 1,1
    queue.append((x,y))
    graph[x][y] = 2
    index = 0
    start_time = 0
    direction = 0 

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx <= n and 1<= ny <= n and graph[nx][ny] != 2:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                queue.append((nx,ny))
            elif graph[nx][ny] == 0:
                graph[nx][ny] =2
                queue.append((nx,ny))
                px, py = queue.popleft()
                graph[px][py] = 0
        else:
            start_time += 1
            break

        x,y = nx, ny
        start_time += 1
        if index < curve_num and start_time == curve[index][0]:
            direction = turn(direction, curve[index][1])
            index += 1
    return start_time

print(simulate())









    
