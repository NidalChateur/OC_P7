import os


def create_folder(folder_path: str):
    """Check if the folder exists; if it does not, create it"""

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


def remove_file(file_path: str):
    """remove an existant old report"""

    if os.path.exists(file_path):
        os.remove(file_path)


def is_existing(folder_path: str) -> bool:
    """Check if the folder exists"""

    if os.path.exists(folder_path):
        return True

    else:
        return False
