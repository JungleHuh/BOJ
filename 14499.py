import sys
input = sys.stdin.readline

N,M,x,y,K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dice = [0]* 6

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in command:

    if i == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif i == 2:
        dice[0], dice[2], dice[3], dice[5] =  dice[2], dice[5], dice[0], dice[3]
    elif i == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    
    nx = x + dx[i-1]
    ny = y + dy[i-1]

    if nx >= N or nx < 0 or ny >= M or ny < 0:
        continue

    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[5]
    else:
        dice[5] = maps[nx][ny]
        maps[nx][ny] = 0

    x = nx
    y = ny

    print(dice[0])



