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
    return line_data

def basin_labeller(line_data: List):

# ----------- Day 9 Part 1 Code -----------------------------------------------------
def check_element(line_data: List):
    max_x_dimension = (len(line_data[0]))
    max_y_dimension = (len(line_data))
    # print(f"Length of X Dimension: {max_x_dimension}")
    # print(f"Length of Y Dimension: {max_y_dimension}")
    # edge_case_count = 0
    risk_level = 0
    for row_index in range(max_y_dimension):
        for column_index in range(max_x_dimension):
            element = line_data[row_index][column_index]
            # print(f"Element: {element}")
            # if row_index == 0 or row_index == max_x_dimension-1 or column_index == 0 or column_index == max_y_dimension-1:
            #     continue

            # look_below = line_data[row_index+1][column_index]
            # look_above = line_data[row_index-1][column_index]
            # look_left = line_data[row_index][column_index-1]
            # look_right = line_data[row_index][column_index+1]

            # print(f"Column Index: {column_index}")
            # print(f"Row Index: {row_index}")
            # print(f"Above: {look_above}")
            # print(f"Below: {look_below}")
            # print(f"Left: {look_left}")
            # print(f"Right: {look_right}")
            # if look_above > element and look_below > element and look_left > element and look_right > element:
            #     risk_level += element + 1
            # edges

            if row_index == 0 and (column_index != 0 and column_index != max_y_dimension-1):
            # if row_index == 0 and (column_index != 0 or column_index != max_y_dimension-1):
            # if row_index == 0 and not (column_index == 0 or column_index == max_y_dimension-1):
                look_below = line_data[row_index+1][column_index]
                look_left = line_data[row_index][column_index-1]
                look_right = line_data[row_index][column_index+1]
                if look_below > element and look_left > element and look_right > element:
                    risk_level += element + 1
                    print("Top Line Edge Case Found")

            elif row_index == max_x_dimension-1 and (column_index != 0 and column_index != max_y_dimension-1):
                look_above = line_data[row_index-1][column_index]
                look_left = line_data[row_index][column_index-1]
                look_right = line_data[row_index][column_index+1]
                if look_above > element and look_left > element and look_right > element:
                    risk_level += element + 1
                    print("Bottom Line Edge Case Found")

            elif column_index == 0 and (row_index != 0 and row_index != max_x_dimension-1):
                look_below = line_data[row_index+1][column_index]
                look_above = line_data[row_index-1][column_index]
                look_right = line_data[row_index][column_index+1]
                if look_above > element and look_below > element and look_right > element:
                    risk_level += element + 1
                    print("Left Side Edge Case Found")
            elif column_index == max_y_dimension-1 and (row_index != 0 and row_index != max_x_dimension-1):
                look_below = line_data[row_index+1][column_index]
                look_above = line_data[row_index-1][column_index]
                look_left = line_data[row_index][column_index-1]
                if look_above > element and look_below > element and look_left > element:
                    risk_level += element + 1
                    print("Right Side Edge Case Found")
            # corners
            elif row_index == 0 and column_index == 0:
                look_below = line_data[row_index+1][column_index]
                look_right = line_data[row_index][column_index+1]
                if look_below > element and look_right > element:
                    risk_level += element + 1
            elif row_index == 0 and column_index == max_y_dimension-1:
                look_below = line_data[row_index+1][column_index]
                look_left = line_data[row_index][column_index-1]
                if look_below > element and look_left > element:
                    risk_level += element + 1
            elif row_index == max_x_dimension-1 and column_index == 0:
                look_right = line_data[row_index][column_index+1]
                look_above = line_data[row_index-1][column_index]
                if look_above > element and look_right > element:
                    risk_level += element + 1
                    print("Corner Edge Case Found")
            elif row_index == max_x_dimension-1 and column_index == max_y_dimension-1:
                look_left = line_data[row_index][column_index-1]
                look_above = line_data[row_index-1][column_index]
                if look_above > element and look_left > element:
                    risk_level += element + 1
            else:
                look_below = line_data[row_index+1][column_index]
                look_above = line_data[row_index-1][column_index]
                look_left = line_data[row_index][column_index-1]
                look_right = line_data[row_index][column_index+1]
                if look_above > element and look_below > element and look_left > element and look_right > element:
                    risk_level += element + 1

    print(f"Risk Level: {risk_level}")
# ------------------------------------------------------------------------------- 


def main():
    data = get_data(FILE_PATH)

if __name__ == "__main__":
    main()

