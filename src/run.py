""" run the brute force method or the dynamic programming method"""

from .read import read
from .bruteforce import brute_force
from .optimized import dynamic_programming
from .output import output
from .view import result
from .draw_graph import graph


def run(file_path: str, capacity: int, method: str):
    """run the brute force or the dynamic programming method
    method in ["brute_force", 'dynamic']"""

    knapsac_capacity = capacity
    scaled = False
    report, input_data = read(file_path)

    if method == "brute_force":
        time_capture, memory_capture, wallets = brute_force(input_data, capacity)

    if method == "dynamic":
        names = list(input_data.keys())
        weights = [input_data[i]["price"] for i in names]
        values = [input_data[j]["value"] for j in names]
        scaled, time_capture, memory_capture, wallets = dynamic_programming(
            names, weights, values, capacity
        )

    output_file_name = output(
        knapsac_capacity, wallets, file_path, input_data, report, method
    )

    result(
        input_data,
        capacity,
        max(time_capture),
        max(memory_capture),
        len(report["excluded lines"]),
        output_file_name,
        scaled,
        method,
    )
    graph(time_capture, memory_capture)
