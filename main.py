from src.mkdir import is_existing, create_folder
from src.controller import controller


def main():
    if is_existing("./src/"):
        create_folder("./input/")
        create_folder("./output/")
        controller()

    else:
        print("\n🛑 The 'src' folder is missing !\n")


if __name__ == "__main__":
    main()
