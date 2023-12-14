n,m = map(int, input().split())
list = []

for i in range(1,n+1):
    list.append(i)

for i in range(m):
    a,b = map(int, input().split())
    temp = list[a-1]
    list[a-1] = list[b-1]
    list[b-1] = temp

for b in list:
    print(b, end = ' ')

    #temp로 교체


