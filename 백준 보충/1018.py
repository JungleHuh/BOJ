import sys
input = sys.stdin.readline

n, m = map(int,input().split())

#n*m 보드에서 8*8 보드로 자를 수 있는 경우의 수가 n-7, m-7이다.
for i in range(n-7):
    for j in range(m-7):
        start_W = 0
        start_B = 0

        for k in range(i,i+8):
            for l in range(j,j+8):
                
