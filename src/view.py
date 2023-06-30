""" view """

from rich.console import Console

from .clear import console_clear


console = Console()
console_width = console.width


def progress_bar(percentage: int):
    """display the progress bar"""

    progress_bar = "█" * percentage + "_" * (100 - percentage)
    if percentage < 100:
        console_clear()
        print(f"\nProgress: {progress_bar} {percentage}%")
        print("\nTo stop the execution of the script, please enter 'Ctrl + C'.")
    if percentage == 100:
        console_clear()
        print(f"\nProgress: {progress_bar} {percentage}%")


def center(text: str) -> str:
    """center the text"""

    title = f"[bold white]{text}[/bold white]"
    spaces = (console_width - len(title)) // 2

    return " " * spaces + title + " " * spaces


def homepage() -> str:
    """display the homepage"""

    centered_text = center("[bold]AlgoInvest & Trad [/bold]")
    line1 = "This script reads a '.xlsx' or '.csv' file as input. It contains a list of stock market actions and"
    line2 = "then returns the most profitable stock portfolio for a given investment amount."

    line3 = "The constraints :\n"
    line4 = "[not bold white]- Each stock can only be purchased once.[/not bold white]"
    line5 = "[not bold white]- The purchase of fractional shares is not possible.[/not bold white]"
    line6 = "[not bold white]- A maximum of 500 euros per customer.[/not bold white]"

    line7 = "continue ? (y/n) > "

    console_clear()
    console.print()
    console.print(centered_text)
    console.print()
    console.print(line1, line2)
    console.print()
    console.print(line3)
    console.print(line4)
    console.print(line5)
    console.print(line6)
    console.print()

    return input(line7)


def input_file() -> str:
    """display the input file conditions"""

    console_clear()
    centered_text = center("[bold white]Step 1 : position your input file[/bold white]")

    line1 = "Place your input file in this folder path : './input/'"
    line2 = "It must be a 'csv' or 'xlsx' file."
    line3 = "The column A must be named : 'name', all stocks name must be unique"
    line4 = "The column B must be named : 'price', all prices must be numbers"
    line5 = "The column C must be named : 'profit', all profits must be numbers"

    navigation = "Navigation :\n"
    next = "[not bold white]1. I have dropped my input file : so go to the next step.[/not bold white]"
    back = "[not bold white]2. Back to the homepage[/not bold white]"

    console.print()
    console.print(centered_text)
    console.print()
    console.print(line1, "\n")
    console.print(line2)
    console.print(line3)
    console.print(line4)
    console.print(line5)
    console.print()
    console.print(navigation)
    console.print(next)
    console.print(back)

    return input("\nyour choice > ")


def select_file(files_path_list: list, folder_path: str) -> list:
    "Display the list of selectable files"

    console_clear()
    centered_text = center("[bold white]Step 2 : select your input file[/bold white]")
    console.print()
    console.print(centered_text)
    console.print()

    i = 1
    for file_path in files_path_list:
        print(" " * 30 + str(i) + ". " + file_path.replace(folder_path, ""))
        i += 1

    print(" " * 30 + str(i) + ". " + "Back to the homepage")
    console.print()

    return input("\nyour choice > ")


def no_file():
    print("\n🛑 No file to select !\n")
    print("\nPlease drop in the 'input' folder a valid file.\n")


def select_method(file_path: str):
    console_clear()
    centered_text = center("[bold white]Step 3 : select your algorithm[/bold white]")
    line1 = "[not bold green]1. The dynamic programming method (recommended)[/not bold green]"
    line2 = (
        "[not bold white]2. The brute force method (not recommended)[/not bold white]"
    )
    line3 = "[not bold white]3. Back to the homepage[/not bold white]"
    console.print()
    console.print(centered_text)
    console.print()
    console.print()
    console.print(" " * 20, "Selected file :", file_path.replace("./input/", ""), "\n")
    console.print(" " * 20, line1)
    console.print(" " * 20, line2)
    console.print(" " * 20, line3)
    console.print()

    return input("\nyour choice > ")


def result(
    input_data: dict,
    capacity: int,
    time_difference: float,
    memory_difference: float,
    errors: int,
    output_file_name: str,
    scaled: bool,
    method: str,
):
    """brute force and dynamic programming view
    input_data: dict for brute force
    input_data: list for dynamic programming
    """
    time_difference = round(time_difference, 2)
    memory_difference = round(memory_difference, 2)
    if len(input_data) > 1:
        print(f"\n{len(input_data)} stocks analyzed.")
    if len(input_data) < 2:
        print(f"\n{len(input_data)} stock analyzed.")

    if errors == 0:
        print("\n🟢 No items were corrupted in the input data.")
    if errors == 1:
        print(f"\n🛑 {errors} item was excluded and registered in the report")
    if errors > 1:
        print(f"\n🛑 {errors} items were excluded and registered in the report")

    print(f"\nThe memory used during the script is {memory_difference} MB.")

    if method == "brute_force":
        print(
            f"\n{2**len(input_data)} combinaisons tested in {time_difference} secs.\n"
        )
        print("Here is the best wallet found using the rigorous and exhaustive")
        print(f"brute force method : '{output_file_name}'\n")

    if method == "dynamic":
        if scaled:
            capacity *= 100
        print(
            f"\n{len(input_data)*capacity} combinaisons tested in {time_difference} secs.\n"
        )
        print("Here is the best wallet found using the dynamic programming")
        print(f"method : '{output_file_name}' \n")
