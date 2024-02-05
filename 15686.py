from itertools import combinations

N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
res = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i+1,j+1))
        elif graph[i][j] == 2:
            chicken.append((i+1,j+1))

res = 1e9
for comb in list(combinations(chicken,M)):
    dist = 0
    for a,b in house:
        temp = 1e9
        for x,y in comb:
            temp = min(temp, abs(a-x)+abs(b-y))
        dist += temp
    res = min(res, dist)
print(res)

