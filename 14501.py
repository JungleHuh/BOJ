import sys
input = sys.stdin.readline
N = int(input())
a = []
b = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    A,B = map(int, input().split())
    a.append(A)
    b.append(B)

for i in range(N-1,-1,-1):
    if a[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[a[i]+i] + b[i])
print(dp[0])
