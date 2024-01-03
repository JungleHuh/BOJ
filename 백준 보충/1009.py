# 1 | 2486 | 3 9 7 1 | 4 6 | 5 | 6 | 7 9 3 1 | 8 4 2 6 | 9 1 | 10 

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a,b = map(int, input().split())
    a = a % 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print(a*a %10)
    else:
        b = b % 4
        if b == 1:
            print(a % 10)
        elif b == 2:
            print(a*a % 10)
        elif b == 3:
            print(a*a*a %10)
        elif b == 0:
            print(a*a*a*a % 10)

