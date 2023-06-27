import os


def clear_console():
    """clear the console under Windows or under [Linux, macOS]"""

    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def progress_bar(percentage: int):
    """display the progress bar"""

    progress_bar = "█" * percentage + "_" * (100 - percentage)
    if percentage < 100:
        clear_console()
        print(f"\nProgress: {progress_bar} {percentage}%")
        print("\nTo stop the execution of the script, please enter 'Ctrl + C'.")
    if percentage == 100:
        clear_console()
        print(f"\nProgress: {progress_bar} {percentage}%")
