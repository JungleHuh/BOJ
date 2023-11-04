t = int(input())
for i in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    total = int(input())

    dp = [0]*(total+1)
    dp[0] = 1

    for coin in coins:
        for i in range(1, total + 1):
            if i >= coin:
                dp[i] += dp[i - coin]

    print(dp[total])