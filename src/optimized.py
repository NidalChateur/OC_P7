""" The Dynamic Programming method to resolve the knapsck problem"""

import time

from psutil import virtual_memory

from .scaler import scaler
from .memory_control import memory_control
from .view import progress_bar


def dynamic_programming(
    names: list, weights: list, values: list, capacity: int
) -> list:
    """return the highest value that the knapsack can achieve and all items
    selected

    'names' is the list of items name
    'weights' is the list of items weight
    'values' is the list of items value
    'capacity' is the capacity of the knapsack"""

    start_memory = virtual_memory().used / (1024**2)
    start_time = time.time()
    memory_capture, time_capture = [], []
    progress = 0
    """ 1. Initialize a table with 'capacity +1' columns and 'len(names)' rows """

    scaled, weights, capacity = scaler(weights, capacity)
    table = [[0] * (capacity + 1) for _ in range(len(names) + 1)]

    """ 2. For each element, iterate over all possible knapsack weights and
    save the highest value that the current knapsack can achieve """

    for i in range(1, len(names) + 1):
        memory_control()
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                table[i][j] = max(
                    table[i - 1][j],
                    table[i - 1][j - weights[i - 1]] + values[i - 1],
                )
            else:
                table[i][j] = table[i - 1][j]

        memory_capture.append(virtual_memory().used / (1024**2) - start_memory)
        time_capture.append(time.time() - start_time)
        if i % 10 == 0:
            progress += (90 / (len(names) + 1)) * 10
            progress_bar(round(progress))
    progress_bar(90)

    """ 3. get the maximum value that the knapsack can achieve  """

    max_value = table[len(names)][capacity]

    """ 4. get the name of all items included in the knapsack """

    selected_items = []
    cost = 0
    j = capacity
    for i in range(len(names), 0, -1):
        if table[i][j] != table[i - 1][j]:
            selected_items.append(names[i - 1])
            cost += weights[i - 1]
            j -= weights[i - 1]

        memory_capture.append(virtual_memory().used / (1024**2) - start_memory)
        time_capture.append(time.time() - start_time)

    progress_bar(100)

    if scaled:
        cost /= 100

    return scaled, time_capture, memory_capture, [[selected_items, cost, max_value]]
