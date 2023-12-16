import sys
import heapq

input = sys.stdin.readline

n = int(input())
roads, data = [], []

for _ in range(n):
    data.append(sorted.list(map(int, input().split())))
road_length = int(input())

# s, e = road: 각 road 리스트의 요소를 s와 e 변수에 언패킹하여 할당합니다. 
# 예를 들어, 만약 road가 (1, 5)라면, s에는 1이 할당되고, e에는 5가 할당
for road in data:
    s, e = road
    if( e - s) <= road_length:
        roads.append(road)

roads.sort(key = lambda x: x[1])

ans = 0
q = []

for road in roads:
    if not q:
        heapq.heappush(q, road)
    else:
        while q[0][0] < road[1] -road_length:
            heapq.heappop(q)
            if not q:
                break
        
        heapq.heappush(q, road)
    ans = max(ans, len(q))

print(ans)

