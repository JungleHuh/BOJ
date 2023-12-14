import sys
input = sys.stdin.readline

n = int(input())
list = []

for i in range(n):
   (a,b) = map(int, input().split())
   list.append((a, b))
#튜플을 일반적인 형태로 출력하는 것이 포인트였던 문제.
list.sort()
for i in range(n):
   print(list[i][0], list[i][1])


