li = []
for i in range(2):
    li.append(list(map(int, input().split())))
print(max(sum(li[0]), sum(li[1])))
