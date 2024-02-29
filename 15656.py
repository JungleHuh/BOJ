def dfs():
    if len(arr) == m:
        print(*arr, end = ' ')
        print()
        return
    for i in s:
        arr.append(i)
        dfs()
        arr.pop()


            

n, m = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
arr = []


dfs()