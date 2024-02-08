import sys
input = sys.stdin.readline
page = [[0 for _ in range(100)]for _ in range(100)]
li = []
counts = 0

N = int(input())
for _ in range(N):
    x,y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            page[i][j] = 1
for k in page:
    counts += k.count(1)
print(counts)
            

