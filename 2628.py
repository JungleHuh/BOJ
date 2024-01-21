N,M = map(int,input().split())
K = int(input())
width = [0,N]
height = [0,M]

for i in range(K):
    a,b = map(int, input().split())
    if a == 0:
        height.append(b)
    elif a == 1:
        width.append(b)

width.sort()
height.sort()
res = 0

for i in range(len(width)-1):
    for j in range(len(height)-1):
        x = width[i+1] -width[i]
        y = height[j+1] - height[j]
        result = max(x*y) 
print(result)