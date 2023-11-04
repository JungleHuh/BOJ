N,K = map(int, input().split())
result = 0
coins = []

for i in range(N):
    coin = int(input())
    coins.append(coin)

coins = sorted(coins, reverse=True)

for coin in coins:
    if coin > K:
        continue
    else:
        while coin <= K:
            K -= coin
            result += 1
            
print(result)