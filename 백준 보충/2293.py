n,k = map(int, input().split())
djs = []
for i in range(n):
    djs.append(int(input()))

dp = [0]* (k+1)
dp[0] = 1

for dj in djs:
    for j in range(dj, k+1):
        dp[j] = dp[j] + dp[j-dj]
print(dp[k])