import sys
input = sys.stdin.readline

n = int(input())
times = [300, 60, 10]
result = 0

for time in times:
    if n % 10 == 0:
        result = n // time 
        n = n % time
        print(result, end = ' ')
        result = 0
    else:
        print(-1)
        break
    
