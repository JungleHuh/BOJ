m,n = map(int, input().split())
cnt = 0

def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)
    
'''
반복문으로 구현
def gcd(m,n):
    while n > 0:
        temp = m % n
        m = n
        n = temp
    return m
'''
def lcm(m,n):
    return m*n // gcd(m,n)


print(gcd(m,n))
print(lcm(m,n))
