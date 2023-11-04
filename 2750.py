N = int(input())
li = []

for i in range(N):
    li.append(int(input()))

for i in range(len(li)):
    for j in range(len(li)):
        if li[i] < li[j]:
            li[i], li[j] = li[j], li[i]

for x in li:
    print(x)



