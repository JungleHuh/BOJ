import sys
input = sys.stdin.readline
dp = []
n = int(input())

for i in range(n):
    dp.append(list(map(int, input().split())))

for a in range(1,n):
    for b in range(i+1):
        if b == 0:
            dp[a][b] += dp[a-1][b]
        elif b == 1:
            dp[a][b] += dp[a-1][b-1]
        else:
            dp[a][b] += max(dp[a-1][b-1], dp[a-1][b])
print(max(dp[n-1]))