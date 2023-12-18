#런타임 에러가 뜸.
import sys
input = sys.stdin.readline

a,b,c = map(float, input().split())

k = a/b
str_k = str(k)
p = str_k.split('.')[1][int(c) - 1]

print(p)



