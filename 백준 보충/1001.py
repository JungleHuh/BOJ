from itertools import combinations

k = int(input())
for i in range(k):
    n,m = map(int, input().split())
    print(combinations(n,m))
