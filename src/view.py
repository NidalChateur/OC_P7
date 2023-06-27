""" view """


def method(
    input_data,
    capacity: int,
    time_difference: float,
    memory_difference: float,
    errors: int,
    output_file_name: str,
    scaled=False,
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

    if isinstance(input_data, dict):
        print(
            f"\n{2**len(input_data)} combinaisons tested in {time_difference} secs.\n"
        )
        print("Here is the best wallet found using the rigorous and exhaustive")
        print(f"brute force method : '{output_file_name}'\n")
    print(scaled)
    if isinstance(input_data, list):
        if scaled:
            capacity*=100
        print(
            f"\n{len(input_data)*capacity} combinaisons tested in {time_difference} secs.\n"
        )
        print("Here is the best wallet found using the dynamic programming")
        print(f"method : '{output_file_name}' \n")
