N = int(input())

for i in range(N):
    for j in range(2, i):
        if i % j == 0:
            break