#! /usr/bin/env python3

from typing import List

FILE_PATH = "day_9/data/input.txt"

def get_data(file_path: str):
    line_data = []
    with open(file_path) as fp:
        for line in fp:
            line = line.rstrip()
            digit_data = []
            for digit in line:
                number = int(digit)
                digit_data.append(number)
            line_data.append(digit_data)
    # print(f"Digit Data = {digit_data}")
    # print(f"Line Data = {line_data}")
    # print(f"Input Data = {line_data}")
    return line_data

def get_max_dimensions(line_data: List):
    max_x_dimension = (len(line_data[0]))
    max_y_dimension = (len(line_data))
    print(f"Length of X Dimension: {max_x_dimension}")
    print(f"Length of Y Dimension: {max_y_dimension}")

# 1. Get max x and max y indexes
# 2. Two nested for loops, one iterating from 0 to xmax, second iterating from 0 to ymax.
# 3. Use double slicing syntax to access a particular element in the square (see example)
# 4. Build model that works on standard digits e.g. all 4 dimensions (doing edge cases later)

def main():
    data = get_data(FILE_PATH)
    get_max_dimensions(data)

if __name__ == "__main__":
    main()

