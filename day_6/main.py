#! /usr/bin/env python3

FILE_PATH = "day_6/data/input.txt"

def get_data(file_path: str):
    input_data = []
    with open(file_path) as fp:
        for line in fp:
            input_data.extend([int(n) for n in line.split(",")])
    return input_data

def main():
    data = get_data(FILE_PATH)
    print(f"test data = {data}")

if __name__=="__main__":
    main()