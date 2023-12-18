#2진수 풀이법
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0 

while n > 0:
    if n & 1:
        cnt +=1
    n >>= 1
print(cnt)

#일반적인 풀이법
