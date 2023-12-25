import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    num = list(map(int, input().split()))
    avg = sum(num[1:])/num[0]
    cnt = 0

    for k in range(1,len(num)):
        if num[k] > avg:
            cnt += 1
    print('%.3f' % (cnt/num[0] * 100) + '%')
