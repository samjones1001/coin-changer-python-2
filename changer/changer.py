def calculate(change_amount):
    denominations = (1, 2, 5, 10, 20, 50, 100, 200)
    for coin in denominations:
        if change_amount == coin:
            return [coin]
    return []