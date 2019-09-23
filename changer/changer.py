import json


def _calculate(change_amount, denominations=(200, 100, 50, 20, 10, 5, 2, 1)):
    for coin in denominations:
        while change_amount >= coin:
            change_amount -= coin
            yield coin


def change(change_amount):
    return [coin for coin in _calculate(change_amount)]


