import sys
input = sys.stdin.readline

li = []
pi = []
ki = []
count = 0

a,b = map(int, input().split())
for i in range(a):
    li.append(input())
for j in range(b):
    pi.append(input())

for i in li:
    for j in pi:
        if i == j:
            count +=1
            ki.append(i)
ki.sort()
print(count)
for x in ki:
    print(x)
    
