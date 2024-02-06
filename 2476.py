import sys
input = sys.stdin.readline
li = []

n = int(input())
for i in range(n):
    a,b,c = map(int, input().split())
    
    if a == b and b == c:
        li.append(10000 + a*1000)
    elif a == b and b != c:
        li.append(1000 + a*100)
    elif a == c and b != c:
        li.append(1000 + a*100)
    elif b == c and a != c:
        li.append(1000 + b*100)
    elif a != b and b != c and a != c:
        max_val = max(a,b,c)
        li.append(max_val*100)
li.sort()
print(li[-1])
    
