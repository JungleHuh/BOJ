

l = []
lst = list(map(int, input().split()))
for i in lst:
    l.append(i*i)
print(sum(l)%10)
