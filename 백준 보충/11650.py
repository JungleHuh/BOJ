import sys
input = sys.stdin.readline

n = int(input())
list = []

for i in range(n):
   (a,b) = map(int, input().split())
   list.append((a, b))

list.sort()
for i in range(n):
   print(list[i][0], list[i][1])


