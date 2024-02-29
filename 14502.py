import sys
input = sys.stdin.readline
N,M= map(int, input().split())

data = [list(map(int, input().split())) for range in N]

temp = [[0]*M for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

res = 0

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx> 0 and nx <N and ny >0 and ny<M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(x,y)
def score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score +=1
    return score

def wall(count):
    global res
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = data[i][j]
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                virus(i,j)
    res = max(res, score())

    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] =1
                count +=1
                wall(count)
                data[i][j] = 0
                count -= 1
wall(0)
print(res)
