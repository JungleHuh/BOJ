import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
a = []
b = []
c = []
d = []

for i in range(n):
    for j in range(n):
        if i > j:
            a.append((graph[i][j]))
        elif i < j :
            b.append((graph[i][j]))
        

for i in range(n):
    k = a[i] + b[i]
    c.append(k)

for i in c:
    for j in c:
        if i-j >= 0:
            d.append(i-j)
print(min(d))
        
    

        

