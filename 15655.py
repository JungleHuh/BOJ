def dfs():
    if len(li) == m:
        print(' '.join(map(str, li)))
        return
    for i in s:
        if visited[i]:
            continue
        if li and li[-1] > i:
            continue
        visited[i] = True
        li.append(i)
        dfs()
        li.pop()
        visited[i] = False
            

n, m = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
visited = [False] * 10000
li = []
i = 0

dfs()