li = []
pi = []
ans = []

for i in range(3):
    a,b = map(int, input().split())
    li.append(a)
    pi.append(b)
li.sort()
pi.sort()

if li[0] == li[1]:
    ans.append(li[2])
elif li[1] == li[2]:
    ans.append(li[0])
else:
    ans.append(li[1])
if pi[0] == pi[1]:
    ans.append(pi[2])
elif pi[1] == pi[2]:
    ans.append(pi[0])
else:
    ans.append(pi[1])

print(*ans)


