import os


def console_clear():
    """clear the console under Windows or under [Linux, macOS]"""

    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def input_cleaner(text: str) -> str:
    """input cleaner"""

    return text.lower().strip()
