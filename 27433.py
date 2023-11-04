def factorial(N):
    if N == 1 or 0:
        return 1
    else:
        return N * factorial(N - 1)

a = int(input())
result = factorial(a)
print(result)