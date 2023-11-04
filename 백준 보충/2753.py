n = int(input())

if n % 4 == 0:
    if not n % 100 == 0:
        if n % 400 == 0:
            print(1)
else:
    print(0)

