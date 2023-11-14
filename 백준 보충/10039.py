l = []
for i in range(5):
    n = int(input())
    if n > 40:
        l.append(n)
    else:
        l.append(40)

print(sum(l)//5)

