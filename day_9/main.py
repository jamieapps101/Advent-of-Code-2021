#! /usr/bin/env python3

FILE_PATH = "day_9/data/input.txt"

def get_data(file_path: str):
    input_data = []
    with open(file_path) as fp:
        for line in fp:
            input_data.append(line[:-1])
    print(f"Input Data = {input_data}")
    return input_data

def main():
    data = get_data(FILE_PATH)

if __name__ == "__main__":
    main()
