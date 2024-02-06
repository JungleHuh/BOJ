from itertools import combinations

N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
comb = []
res = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i+1,j+1))
        elif graph[i][j] == 2:
            chicken.append((i+1,j+1))

min_dist = 1e9
for selected in combinations(chicken,M):
    dist = 0
    for a,b in house:
        temp = 1e9
        for i,j in selected:
            temp = min(temp, abs(a-i)+abs(b-j))
        dist += temp
    min_dist = min(min_dist,dist)
print(min_dist)
