cache = [0]* 11
cache[1] = 1
cache[2] = 2
cache[3] = 4
cache[4] = 7

for i in range(5,11):
    cache[i] = sum(cache[i-3:i])

T = int(input())
for _ in range(T):
    a = int(input())
    print(cache[a])