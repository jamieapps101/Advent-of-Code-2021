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

# need a number of basins counter (to track total number)
# also need to count the number of digits within each basin
# for digit in line
# if digit = 9 - go to next line (but this would lose basins further to the right in the data??)
# else current_basin_counter += 1

# Ok, so what about, instead of line 25: if digit < 9, look around at surrounding measurements
# if the surronding measurement is in a basin, and has been assigned a basin, then assign the current
# measurement to the same basin. otherwise assign the current measurement to a new basin id?

def main():
    data = get_data(FILE_PATH)

if __name__ == "__main__":
    main()

