""" The Brute Force method to resolve the knapsck problem
    - Integer knapsack capacity
    - Integer weights"""

from itertools import combinations
import time

from psutil import virtual_memory
import pandas as pd

from .read import read
from .memory_control import memory_control
from .progress_bar import progress_bar
from .output import output
import src.view
from .draw_graph import graph


def brute_force(input_data: dict, capacity: int) -> list:
    """generate all possible wallets with a maximum constraint of
    [capacity]."""

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


def run(file_path: str, capacity: int):
    """run the brute force method
    'path : str' is the path of the input data
    'capacity : int' is the capacity of the knapsack"""

    report, input_data = read(file_path)
    time_capture, memory_capture, wallets = brute_force(input_data, capacity)
    output_file_name = output(wallets, file_path, input_data, report, "brute_force")

    src.view.method(
        input_data,
        capacity,
        max(time_capture),
        max(memory_capture),
        len(report["excluded lines"]),
        output_file_name,
    )
    graph(time_capture, memory_capture)
