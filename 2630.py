import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = [0, 0]

def find_paper(x,y,N):
    color = paper[x][y]
    for row in range(x, x+N):
        for col in range(y, y+N):
            if color != paper[row][col]:
                find_paper(x,y, N//2)
                find_paper(x,y+N//2, N//2)
                find_paper(x+N//2,y, N//2)
                find_paper(x+N//2, y+N//2, N//2)
                return 0
            
    if color == 0:
        ans[0] += 1
    else:
        ans[1] += 1

find_paper(0,0,N)
for a in ans:
    print(a)

