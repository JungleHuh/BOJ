import sys
import heapq

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key= lambda x: (x[1], x[0]))

time = 0
ans = 0

for meeting in meetings:
    if time <= meeting[0]:
        #튜플임을 명심하자.
        time = meeting[1]
        ans += 1
print(ans)



