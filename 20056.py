N,M,K = map(int, input().split())
ball = []
for i in range(M):
    r,c,m,s,d = list(map(int, input().split()))
    ball.append([r-1,c-1,m,s,d])

graph = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    while ball:
        cr,cc,cm,cs,cd = ball.pop(0)
        nr = (cr + cs*dx[cd]) %N
        nc = (cc + cs*dy[cd]) %N
        graph[nr][nc].append([cm,cs,cd])

    for r in range(N):
        for c in range(N):
            if len(graph[r][c]) >1:
                sum_m,sum_s,cnt_odd,cnt_even,cnt = 0,0,0,0,len(graph[r][c])
                while graph[r][c]:
                    _m,_s,_d = graph[r][c].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd +=1
                    else:
                        cnt_even +=1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0,2,4,6]
                else:
                    nd = [1,3,5,7]
                if sum_m//5:
                    for d in nd:
                        ball.append([r,c,sum_m//5,sum_s//cnt,d])
            if len(graph[r][c]) == 1:
                ball.append([r,c] + graph[r][c].pop())
print(sum([f[2] for f in ball]))

                    





