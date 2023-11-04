N, M = map(int, input().split())
num = list(map(int, input().split()))
numlist = []


for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            three = numlist[i] + numlist[j] + numlist[k]

            if three > M:
                continue
            else:
                numlist.append(three)
print(max(numlist))


    


