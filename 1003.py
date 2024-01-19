T = int(input())
for _ in range(T):
    fib = int(input())
    a,b = 1, 0 
    for i in range(fib):
        a,b = b, a+b
    print(a,b)