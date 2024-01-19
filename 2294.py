n,k = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

dp = [100001 for i in range(k+1)]
dp[0] = 0

for coin in arr:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[k])