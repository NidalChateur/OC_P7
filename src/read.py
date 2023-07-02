""" read csv, xlsx files and generate an error report  """

import sys
import csv
import numpy as np

import pandas as pd
from pandas import DataFrame

from .view import key_error, no_value


def duplicate_detecter(data_frame: DataFrame, line_number: int, file_type: str):
    """check the presence of the duplicates stock name"""

    duplicates = []
    stocks_name = []
    for i in range(line_number):
        try:
            if file_type == "csv":
                if data_frame.loc[i, "name"] not in stocks_name:
                    stocks_name.append(data_frame.loc[i, "name"])
                else:
                    duplicates.append(data_frame.loc[i, "name"])
            if file_type == "xlsx":
                if data_frame.at[i, "name"] not in stocks_name:
                    stocks_name.append(data_frame.at[i, "name"])
                else:
                    duplicates.append(data_frame.at[i, "name"])
        except KeyError:
            key_error()
            sys.exit()

    return duplicates


def test_no_data(stocks: dict):
    """check the stocks number and stop the script if len ==0"""

    if len(stocks) == 0:
        no_value()
        sys.exit()


def is_digit(value) -> bool:
    """test if 'value' is an integer or a float
    value refers to 'price' or 'profit'"""

    if isinstance(value, float) or isinstance(value, int):
        return True

    if isinstance(value, np.float64) or isinstance(value, np.int64):
        return True

    if isinstance(value, str):
        if value.replace(",", "").replace(".", "").strip().isdigit():
            return True

    else:
        return False


def is_nan(stock_name, price, profit) -> bool:
    """check if paramaters are NaN (not a number)"""

    if isinstance(stock_name, float):
        if np.isnan(stock_name):
            return True

    if isinstance(price, float):
        if np.isnan(price):
            return True

    if isinstance(profit, float):
        if np.isnan(profit):
            return True

    else:
        return False


def number_converter(price, profit) -> float:
    """convert 'price' and 'profit' to float or int"""

    if isinstance(price, str):
        price = price.replace(",", ".").strip()
        if "." in price:
            price = round(float(price), 2)
        else:
            price = int(price)

    if isinstance(profit, str):
        profit = profit.replace(",", ".").strip()
        if "." in profit:
            profit = round(float(profit), 2)
        else:
            profit = int(profit)

    return round(price, 2), round(profit, 2)


def detect_delimiter(file_path: str) -> str:
    """detect the csv delimiter using the sniff() function from the
    csv module"""

    with open(file_path, "r") as file:
        dialect = csv.Sniffer().sniff(file.read(1024))
        delimiter = dialect.delimiter

    return delimiter


def read_csv_xlsx(file_path: str) -> DataFrame:
    """choose the appropriate method to read the file"""

    if file_path[-3:] == "csv":
        delimiter = detect_delimiter(file_path)

        return "csv", pd.read_csv(file_path, sep=delimiter)

    if file_path[-4:] == "xlsx":
        return "xlsx", pd.read_excel(file_path)


def data_line(data_frame: DataFrame, i: int, file_type: str) -> str:
    try:
        if file_type == "csv":
            return (
                data_frame.loc[i, "name"],
                data_frame.loc[i, "price"],
                data_frame.loc[i, "profit"],
            )

        if file_type == "xlsx":
            return (
                data_frame.at[i, "name"],
                data_frame.at[i, "price"],
                data_frame.at[i, "profit"],
            )
    except KeyError:
        key_error()
        sys.exit()


def read(file_path: str) -> dict:
    """read a '.csv' or a '.xlsx' file and convert it into a dictionary.
    filter invalid values and create a report error if there is"""

    report = {"excluded lines": [], "error description": []}
    stocks = {}
    file_type, data_frame = read_csv_xlsx(file_path)
    line_number = data_frame.shape[0]
    duplicates = duplicate_detecter(data_frame, line_number, file_type)
    for i in range(line_number):
        stock_name, price, profit = data_line(data_frame, i, file_type)

        if is_nan(stock_name, price, profit):
            report["excluded lines"].append(i + 2)
            report["error description"].append("stock_name, price or profit is null")
            continue

        if stock_name in duplicates:
            report["excluded lines"].append(i + 2)
            report["error description"].append(f"{stock_name} is a duplicate")
            continue

        if not is_digit(price):
            report["excluded lines"].append(i + 2)
            report["error description"].append("price is not a number")
            continue

        if not is_digit(profit):
            report["excluded lines"].append(i + 2)
            report["error description"].append("profit is not a number")
            continue

        price, profit = number_converter(price, profit)

        if price <= 0 or profit <= 0:
            report["excluded lines"].append(i + 2)
            report["error description"].append("price <= 0 or profit <= 0")
            continue

        stocks[stock_name] = {
            "price": price,
            "value": round(price * (1 + (profit / 100)), 2),
        }

    test_no_data(stocks)

    return report, stocks
