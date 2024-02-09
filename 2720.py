import sys
input = sys.stdin.readline
count = [25,10,5,1]
T = int(input())

for _ in range(T):
    n = int(input())
    for i in count:
        print(n//i, end = " ")
        n = n%i

