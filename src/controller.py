""" controller """

import sys
import os

from .view import homepage, input_file, select_file, select_method, no_file
from .clear import input_cleaner
from .run import run


def controller():
    """main controller and homepage controller"""

    running = True
    while running:
        reponse1 = homepage()
        reponse1 = input_cleaner(reponse1)

        if reponse1 == "y":
            input_file_controller()
        if reponse1 != "y":
            running = False
            sys.exit()


def input_file_controller():
    """input_file controller"""

    reponse = input_file()
    reponse = input_cleaner(reponse)
    if reponse == "1":
        file_selecter_controller()

    if reponse == "2":
        controller()

    if reponse not in ["1", "2"]:
        input_file_controller()


def file_selecter_controller():
    """select_file controller"""

    folder_path = "./input/"
    files = os.listdir(folder_path)
    files_path_list = []
    for file in files:
        file_path = os.path.join(folder_path, file)
        if file_path.endswith(".csv") or file_path.endswith(".xlsx"):
            files_path_list.append(file_path)

    if len(files_path_list) > 0:
        reponse = select_file(files_path_list, folder_path)
        reponse = input_cleaner(reponse)

        if reponse.isdigit():
            if int(reponse) in range(1, len(files_path_list) + 1):
                file_path = files_path_list[int(reponse) - 1]
                method_selecter_controller(file_path)

            if int(reponse) == len(files_path_list) + 1:
                controller()

            if int(reponse) not in range(1, len(files_path_list) + 1):
                file_selecter_controller()

        if not reponse.isdigit():
            file_selecter_controller()

    else:
        no_file()
        return "exit"


def method_selecter_controller(file_path: str):
    """select_method controller"""

    reponse = select_method(file_path)
    reponse = input_cleaner(reponse)
    if reponse == "1":
        run(file_path, 500, "dynamic")
    if reponse == "2":
        run(file_path, 500, "brute_force")
    if reponse == "3":
        controller()
    if reponse not in ["1", "2", "3"]:
        method_selecter_controller(file_path)
