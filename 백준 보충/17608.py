import sys
input = sys.stdin.readline

n = int(input())
stack = []
cnt = 0
max = 0

for i in range(n):
    stack.append(int(input()))

while stack:
    top = stack.pop()
    if top > max:
        max = top
        cnt += 1
print(cnt)

