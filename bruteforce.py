import pandas as pd


def load() -> dict:
    """read the table of data and convert it into dict"""

    actions = {}
    data_frame = pd.read_excel("./test.xlsx")
    line_number = data_frame.shape[0]
    for i in range(line_number):
        actions[data_frame.at[i, "name"]] = {
            "price": data_frame.at[i, "price"],
            "profit": data_frame.at[i, "profit"],
        }

    return actions


def add_1(binary_number: str) -> str:
    """add 1 to a binary number and return the sum"""

    decimal_number = int(str(binary_number), 2) + 2**0

    return bin(decimal_number).replace("0b", "").zfill(len(load()))


def max() -> str:
    """determine the maximum number of possibilities in binary"""

    number = ""
    for i in range(len(load())):
        number += "1"

    return number


def possibilities() -> list:
    """check all possibilities without constraints"""

    all_possibilities = []
    possibility = add_1(0)
    while possibility != add_1(max()):
        combination = []
        index = 1

        for p in reversed(possibility):
            if p == "1":
                combination.append(
                    [
                        f"Action-{index}",
                        load()[f"Action-{index}"]["price"],
                        load()[f"Action-{index}"]["profit"],
                    ]
                )
            index += 1

        all_possibilities.append(combination)
        possibility = add_1(possibility)

    return all_possibilities


def sort_possibilities():
    """sort all possibilities by profit with the price constraints < 500
    then export the result as excel file"""

    all_combinations = []
    index = 1
    for p in possibilities():
        benefit = 0
        price = 0
        for j in p:
            price += j[1]
            benefit += j[2]
        if price < 500:
            all_combinations.append([f"combi {index}", p, price, round(benefit, 2)])
        index += 1
    for h in sorted(all_combinations, key=lambda w: (-w[3])):
        print(h)
    data = [
        {"actions": d[1], "price": d[2], "benefit": d[3]}
        for d in sorted(all_combinations, key=lambda w: (-w[3]))
    ]
    data_to_export = pd.DataFrame.from_records(data)
    data_to_export.to_excel("./output.xlsx")


sort_possibilities()
