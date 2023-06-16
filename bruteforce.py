from itertools import combinations
import time

import pandas as pd


def load(path="./input/data.xlsx") -> dict:
    """read the table of data and convert it into dict"""

    stocks = {}
    data_frame = pd.read_excel(path)
    line_number = data_frame.shape[0]
    for i in range(line_number):
        stocks[data_frame.at[i, "name"]] = {
            "price": data_frame.at[i, "price"],
            "profit": data_frame.at[i, "profit"],
        }

    return stocks


def possible_wallets(input_data: dict, max=500) -> list:
    """Generate all possible wallets with a maximum constraint of [500]."""

    data = input_data
    cost, value = 0, 0
    wallets = []
    for i in range(0, len(data) + 1):
        solutions = list(combinations(list(data.keys()), i))
        for wallet in solutions:
            for stock in wallet:
                cost += data[stock]["price"]
                value += data[stock]["price"] * (1 + data[stock]["profit"])
            if cost <= max:
                wallets.append([wallet, cost, value])
            cost, value = 0, 0

    return wallets


def output(wallets: list):
    """sort the wallets list and write the best wallet in an Excel file"""

    output_data = [
        {"the best wallet": d[0], "cost": d[1], "value after 2 years": d[2]}
        for d in sorted(wallets, key=lambda w: (-w[2]))[:1]
    ]
    data_to_export = pd.DataFrame.from_records(output_data)
    data_to_export.to_excel("./output/output_brute_force.xlsx", index=False)


def brute_force():
    """run the brute force method"""

    start = time.time()
    input_data = load()
    wallets = possible_wallets(input_data)
    output(wallets)
    end = time.time()
    print(f"\n{2**len(input_data)} combinaisons tested in {end-start} secs.\n")
    print("Here is the best wallet found using the rigorous and exhaustive")
    print("brute force method : ./output/output_brute_force.xlsx\n")


brute_force()
