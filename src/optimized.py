""" The Dynamic Programming method to resolve the knapsck problem"""

import time
import numpy as np

from psutil import virtual_memory

from .read import read
from .memory_control import memory_control
from .progress_bar import progress_bar
from .output import output
import src.view
from .draw_graph import graph


def is_int(prices: list) -> bool:
    """check if price type is int"""

    for i in prices:
        if not isinstance(i, int) or not isinstance(i, np.int64):
            return False

    return True


def scaler(prices: list, capacity: int) -> list:
    scaled = False
    if not is_int(prices):
        for i in range(len(prices)):
            prices[i] = int(prices[i] * 100)
        capacity *= 100
        scaled = True

    return scaled, prices, int(capacity)


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

    max_value = table[len(names)][capacity]
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


def run(file_path: str, capacity: int):
    """run the dynamic programming method
    'path : str' is the path of the input data
    'capacity : int' is the capacity of the knapsack"""

    report, input_data = read(file_path)
    names = list(input_data.keys())
    weights = [input_data[i]["price"] for i in names]
    values = [input_data[j]["value"] for j in names]
    scaled, time_capture, memory_capture, wallet = dynamic_programming(
        names, weights, values, capacity
    )
    output_file_name = output(wallet, file_path, input_data, report, "dynamic")

    src.view.method(
        names,
        capacity,
        max(time_capture),
        max(memory_capture),
        len(report["excluded lines"]),
        output_file_name,
        scaled,
    )
    graph(time_capture, memory_capture)
