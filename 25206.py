li = []
total = []

for _ in range(20):
    a,b,c = map(str, input().split())
    if c == 'A+':
        k = 4.5 * float(b)
        li.append(k)
        total.append(float(b))
    elif c == 'A0':
        k = 4.0 * float(b)
        li.append(k)
        total.append(float(b))
    elif c == 'B+':
        k = 3.5 * float(b)
        li.append(k)
        total.append(float(b))
    elif c == 'B0':
        k = 3.0 * float(b)
        li.append(k)
        total.append(float(b))
    elif c == 'C+':
        k = 2.5 * float(b)
        li.append(k)
        total.append(float(b))
    elif c == 'C0':
        k = 2.0 * float(b)
        li.append(k)
        total.append(float(b))
    elif c == 'D+':
        k = 1.5 * float(b)
        li.append(k)
        total.append(float(b))
    elif c == 'D0':
        k = 1.0 * float(b)
        li.append(k)
        total.append(float(b))
    elif c == 'F':
        k = 0
        li.append(k)
        total.append(float(b))
    elif c == 'P':
        k = 0
        li.append(k)

print(sum(total))
print(sum(li)/sum(total))

        