import numpy as np


def is_int(prices: list) -> bool:
    """check if price type is int"""

    for i in prices:
        if not isinstance(i, int) and not isinstance(i, np.int64):
            return False

    return True


def scaler(prices: list, capacity: int) -> list:
    """scale float number to int"""

    scaled = False
    if not is_int(prices):
        for i in range(len(prices)):
            prices[i] = int(prices[i] * 100)
        capacity = (capacity * 100) - 2
        scaled = True

    return scaled, prices, int(capacity)
