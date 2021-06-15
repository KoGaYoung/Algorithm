money = int(input())
money = 1000 - money
coin_count = 0
coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    if money == 0:
        break
    coin_count += money // coin
    money %= coin

print(coin_count)