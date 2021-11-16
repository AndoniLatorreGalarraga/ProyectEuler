def stack(prev, value):
    if value == 200: return 1
    if value > 200: return 0
    ans = 0
    for coin in [200, 100, 50, 20, 10, 5, 2, 1]:
        if coin <= prev:
            ans += stack(coin, value + coin)
    return ans

print(stack(200, 0))