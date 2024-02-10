N,M = map(int, input().split())
count = 0

while M != N:
    if N >M:
        count =- 2
        break
    if str(M)[-1] == '1':
        M = M//10
        count +=1
    elif M % 2 == 0:
        M = M//2
        count +=1
    else:
        count =- 2
        break
print(count+1)
