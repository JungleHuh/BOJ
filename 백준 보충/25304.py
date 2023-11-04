X = int(input())
N = int(input())
list = []

for i in range(N):
    A,B = map(int, input().split())
    C = A * B 
    list.append(C)

if sum(list) == X:
    print('Yes')
else:
    print('NO')
