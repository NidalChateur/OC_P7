from src.mkdir import is_existing, create_folder
import src.bruteforce
import src.optimized


def main():
    if is_existing("./src/"):
        create_folder("./input/")
        create_folder("./output/")
        # src.bruteforce.run(file_path="./input/dataset0.csv", capacity=500)
        # src.bruteforce.run(file_path="./input/dataset0.csv", capacity=500)
        src.optimized.run(file_path="./input/dataset2.xlsx", capacity=500)
        # src.optimized.run(file_path="./input/dataset1.csv", capacity=500)
    else:
        print("\n🛑 The 'src' folder is missing !\n")


if __name__ == "__main__":
    main()
