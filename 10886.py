n = int(input())
a = []
b = []
for _ in range(n):
    m = int(input())
    if m == 1:
        a.append(m)
    else:
        b.append(m)

if len(a) > len(b):
    print( "Junhee is cute!")
elif len(a) < len(b):
    print( "Junhee is not cute!")