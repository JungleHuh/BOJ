import sys
input = sys.stdin.readline

N,M,x,y,K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dice = [0]* 6

dx = [0,0,-1,1]
dy = [1,-1,0,0]


for i in range(K):
    dir = command[i] - 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if not 0 <= nx < N or not 0 <= ny < M:
        continue

    if dir == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1:
        dice[0], dice[2], dice[3], dice[5] =  dice[2], dice[5], dice[0], dice[3]
    elif dir == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[5]
    else:
        dice[5] = maps[nx][ny]
        maps[nx][ny] = 0

    x = nx
    y = ny

    print(dice[0])



