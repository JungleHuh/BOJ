N,M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))
print(graph)
for j in range(M):
    move = tuple(map(int, input().split()))


