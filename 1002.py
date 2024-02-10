N, M = map(int, input().split())
arr = []

for i in range(N, M + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i != 1:
        arr.append(i)

for k in arr:
    print(k)