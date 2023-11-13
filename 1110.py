import sys
N = int(sys.stdin.readline().strip())
k = N
count = 0

while True:
    a = N //10
    b = N % 10
    c = 10 * b + ((a + b) % 10)
    count += 1
    if c == k:
        break
    else:
        N = c

print(count)
