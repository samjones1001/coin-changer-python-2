from collections import Iterable
from typing import List


def _convert(change_amount: int) -> Iterable:
    for coin in [200, 100, 50, 20, 10, 5, 2, 1]:
        while change_amount >= coin:
            change_amount -= coin
            yield coin


def change(change_amount: int) -> List[int]:
    return [coin for coin in _convert(change_amount)]
