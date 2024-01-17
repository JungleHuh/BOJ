def dfs():
    if len(com) == M:
        print(*com)
        return
    pre = 0

    for i in range(len(arr)):
        if visited[i] == 0 and pre != arr[i]:
            com.append(arr[i])
            visited[i]  = 1
            pre = arr[i]
            dfs()
            visited[i] = 0
            com.pop()


N,M = map(int, input().split())
arr = list(map( int, input().split()))
arr.sort()
com = []
visited = [0]* (N+1)
dfs()



