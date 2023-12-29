import sys
input = sys.stdin.readline

a,b = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

for i in list_a:
    for j in list_b:
        if i == j:
            list_a.remove(i)
            print(list_a)
            

