import json





def calculate(change_amount, denominations=(200, 100, 50, 20, 10, 5, 2, 1)):
    coins = []
    for coin in denominations:
        while change_amount >= coin:
            change_amount -= coin
            coins.append(coin)
    return coins


