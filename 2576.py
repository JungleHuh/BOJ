li = []
k = []

for i in range(7):
    li.append(int(input()))
    
for odd in li:
    if odd % 2 != 0:
        k.append(odd)

k.sort()

if k: 
    print(sum(k))
    print(k[0])
else:
    print(-1)
        