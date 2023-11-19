n,m = map(int, input().split())

if m - 45 < 0:
    if n == 0:
        print(23, end = ' ')
        print(m+15)
    else:
        print(n-1, end = ' ')
        print(m+15)

else:
    print(n, end = ' ')
    print(m-45)