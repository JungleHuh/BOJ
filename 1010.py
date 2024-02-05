from itertools import combinations
from math import comb

n = int(input())
for i in range(n):
    m = list(map(int, input().split()))
    m.sort(reverse=True)
    result = comb(*m) 
    print(result)