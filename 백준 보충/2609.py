m,n = map(int, input().split())
cnt = 0

def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)
def lcm(m,n):
    return m*n // gcd(m,n)


print(gcd(m,n))
print(lcm(m,n))
