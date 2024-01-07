import sys
input = sys.stdin.readline

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

k = list(input())
res = 0

for i in k:
    for j in dial:
        if i in str(j):
            num = dial.index(j) + 3
            res += num
print(res)

