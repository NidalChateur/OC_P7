import time

import pandas as pd


def load_csv(path: str) -> list:
    names, weights, values = [], [], []
    data_frame = pd.read_csv(path)
    line_number = data_frame.shape[0]
    for i in range(line_number):
        names.append(data_frame.loc[i, "name"])
        weights.append(data_frame.loc[i, "price"])
        values.append(data_frame.loc[i, "profit"])

    return names, weights, values


def load_xlsx(path: str) -> list:
    """read the table.xlsx and return it as 3 lists :
    list of names, list of weights, list of values"""

    names, weights, values = [], [], []
    data_frame = pd.read_excel(path)
    line_number = data_frame.shape[0]
    for i in range(line_number):
        names.append(data_frame.at[i, "name"])
        weights.append(data_frame.at[i, "price"])
        values.append(
            round(data_frame.at[i, "price"] * (1 + data_frame.at[i, "profit"]), 2)
        )

    return names, weights, values


def knapsack_dynamic(names: list, weights: list, values: list, capacity: int) -> list:
    """return the highest value that the knapsack can achieve and all items
    selected

    'names' is the list of items name
    'weights' is the list of items weight
    'values' is the list of items value
    'capacity' is the capacity of the knapsack"""

    """ 1. Initialize a table with 'capacity +1' columns and 'len(names)' rows """

    number_of_items = len(names)
    table = [[0] * (capacity + 1) for _ in range(number_of_items + 1)]

    """ 2. For each element, iterate over all possible knapsack weights and 
    save the highest value that the current knapsack can achieve """

    for i in range(1, number_of_items + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                table[i][j] = max(
                    table[i - 1][j], table[i - 1][j - weights[i - 1]] + values[i - 1]
                )
            else:
                table[i][j] = table[i - 1][j]

    """ 3. get the maximum value that the knapsack can achieve  """

    max_value = table[number_of_items][capacity]

    """ 4. get the name of all items included in the knapsack """

    max_value = table[number_of_items][capacity]
    selected_items = []
    j = capacity
    for i in range(number_of_items, 0, -1):
        if table[i][j] != table[i - 1][j]:
            selected_items.append(names[i - 1])
            j -= weights[i - 1]

    return max_value, selected_items


def output(max_value: float, selected_items: list, capacity: int):
    output_data = [
        {
            "the best wallet": selected_items,
            "cost": capacity,
            "value after 2 years": max_value,
        }
    ]
    data_to_export = pd.DataFrame.from_records(output_data)
    data_to_export.to_excel("./output/output_dynamic.xlsx", index=False)


def run_knapsack_dynamic(path="./input/dataset0.csv", capacity=500):
    start = time.time()
    names, weights, values = load_csv(path)
    max_value, selected_items = knapsack_dynamic(names, weights, values, capacity)
    output(max_value, selected_items, capacity)
    end = time.time()
    print(f"\n{len(names)*capacity} combinaisons tested in {end-start} secs.\n")
    print("Here is the best wallet found using the dynamic programming")
    print("method : ./output/output_dynamic.xlsx \n")


run_knapsack_dynamic()
