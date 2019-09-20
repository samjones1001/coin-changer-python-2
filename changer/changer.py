def calculate(change_amount, coins=None):
    if coins is None: coins = []
    for coin in (200, 100, 50, 20, 10, 5, 2, 1):
        if change_amount >= coin:
            change_amount -= coin
            coins.append(coin)
    return coins
