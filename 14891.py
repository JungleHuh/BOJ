import collections
top = []

for _ in range(4):
    top.append(collections.deque(list(input())))
k = int(input())
r = [list(map(int, input().split())) for _ in range(k)]

def left(num, dir):
    if num <0:
        return
    if top[num][2] != top[num+1][6]:
        left(num-1, -dir)
        top[num].rotate(dir)

def right(num,dir):
    if num > 3:
        return
    if top[num][6] != top[num-1][2]:
        right(num+1, -dir)
        top[num].rotate(dir)

for i in range(k):
    num = r[i][0]-1
    dir = r[i][1]
    left(num-1,-dir)
    right(num+1,-dir)
    top[num].rotate(dir)

res = 0

if top[0][0] == '1':
    res += 1
if top[1][0] == '1':
    res += 2
if top[2][0] == '1':
    res += 4
if top[3][0] == '1':
    res += 8

print(res)
