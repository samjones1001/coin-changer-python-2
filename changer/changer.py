from collections.abc import Iterable
from typing import List


def _calculate(change_amount: int, denominations=(200, 100, 50, 20, 10, 5, 2, 1)) -> Iterable:
    for coin in denominations:
        while change_amount >= coin:
            change_amount -= coin
            yield coin


def change(change_amount: int) -> List[int]:
    return [coin for coin in _calculate(change_amount)]


