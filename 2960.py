N,M = map(int, input().split())

arr = [False] * (N+1)
count = 0

for i in range(2, N+1):
    for j in range(i, N+1, i):
        if arr[j] == False:
            arr[j] = True
            count += 1
            if count == M:
                print(j)
                break





