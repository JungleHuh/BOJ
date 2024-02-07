import sys
input = sys.stdin.readline

N,M = map(int, input().split())

int_key = {}
name_key = {}

for i in range(1,N+1):
    name = input().rstrip()
    int_key[i] = name
    name_key[name] = i

for _ in range(M):
    item = input().rstrip()
    if item.isdigit() == True:
        print(int_key[int(item)])
    else:
        print(name_key[item])