def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start,n):
        temp.append(s[i])
        dfs(i)
        temp.pop()


            

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
temp = []

dfs(0)