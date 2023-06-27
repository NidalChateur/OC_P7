""" manage the output file """

import pandas as pd

from .mkdir import remove_file


def output(
    wallets: list, file_path: str, input_data: dict, report: dict, method: str
) -> str:
    """sort the wallets list and write the best wallet in an Excel file
    generate a report error"""

    wallets = sorted(wallets, key=lambda w: (-w[2]))[:1]
    output_1 = [
        {
            "the best wallet": d[0],
            "total cost": d[1],
            "total value": d[2],
            "total return": d[2] - d[1],
            "report": len(report["excluded lines"]),
        }
        for d in wallets
    ]
    output_2 = [
        {
            "name": stock,
            "cost": input_data[stock]["price"],
            "value": input_data[stock]["value"],
            "return": input_data[stock]["value"] - input_data[stock]["price"],
        }
        for stock in wallets[0][0]
    ]
    file_name = (
        file_path.replace("./input/", "").replace(".csv", "").replace(".xlsx", "")
    )
    df1 = pd.DataFrame(output_1)
    df2 = pd.DataFrame(output_2)
    df3 = pd.DataFrame(report)
    remove_file(f"./output/{method}_{file_name}.xlsx")
    writer = pd.ExcelWriter(f"./output/{method}_{file_name}.xlsx", engine="xlsxwriter")

    df1.to_excel(writer, sheet_name="global", index=False)
    df2.to_excel(writer, sheet_name="choosen stocks", index=False)
    df3.to_excel(writer, sheet_name="report", index=False)
    writer.close()

    return f"./output/dynamic_{file_name}.xlsx"
