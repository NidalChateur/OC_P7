""" The Brute Force method to resolve the knapsck problem"""

from itertools import combinations
import time
import sys

from psutil import virtual_memory


from .memory_control import memory_control
from .view import progress_bar


def maximum_limit(input_data: dict):
    if len(input_data) > 20:
        print(
            "\n🛑 Do not exceed a maximum of 20 items when running the brute force method.\n"
        )
        sys.exit()


def brute_force(input_data: dict, capacity: int) -> list:
    """generate all possible wallets with a maximum constraint of
    [capacity]."""

    maximum_limit(input_data)
    start_memory = virtual_memory().used / (1024**2)
    start_time = time.time()
    memory_capture, time_capture = [], []
    progress = 0

    data = input_data
    cost, value = 0, 0
    wallets = []
    for i in range(0, len(data) + 1):
        memory_control()
        solutions = list(combinations(list(data.keys()), i))
        for wallet in solutions:
            for stock in wallet:
                cost += data[stock]["price"]
                value += data[stock]["value"]
            if cost <= capacity:
                wallets.append([wallet, cost, value])
            cost, value = 0, 0

        memory_capture.append(virtual_memory().used / (1024**2) - start_memory)
        time_capture.append(time.time() - start_time)
        progress += round(100 / (len(data) + 2))
        progress = min(100, progress)
        progress_bar(progress)
    progress_bar(100)

    return time_capture, memory_capture, wallets
