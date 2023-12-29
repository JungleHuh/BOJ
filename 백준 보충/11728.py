import sys
input = sys.stdin.readline

a,b = map(int, input().split())

first = list(map(int, input().split()))
second = list(map(int, input().split()))

for i in second:
    first.append(i)
set(first)
k = sorted(first)
print(k)

for i in k:
    print(i, end = ' ')
