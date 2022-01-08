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

# def get_max_dimensions(line_data: List):
#     max_x_dimension = (len(line_data[0]))
#     max_y_dimension = (len(line_data))
#     print(f"Length of X Dimension: {max_x_dimension}")
#     print(f"Length of Y Dimension: {max_y_dimension}")
#     return max_x_dimension, max_y_dimension

def access_element(line_data: List):
    max_x_dimension = (len(line_data[0]))
    max_y_dimension = (len(line_data))
    print(f"Length of X Dimension: {max_x_dimension}")
    print(f"Length of Y Dimension: {max_y_dimension}")
    # edge_case_count = 0
    for row_index in range(max_y_dimension):
        for column_index in range(max_x_dimension):
            element = line_data[row_index][column_index]
            # print(f"Element: {element}")
            look_above = line_data[row_index-1][column_index]
            look_below = line_data[row_index+1][column_index]
            look_left = line_data[row_index][column_index-1]
            look_right = line_data[row_index][column_index+1]
            # print(f"Column Index: {column_index}")
            # print(f"Row Index: {row_index}")
            print(f"Above: {look_above}")
            print(f"Below: {look_below}")
            print(f"Left: {look_left}")
            print(f"Right: {look_right}")

            if row_index == 0 or row_index == max_x_dimension-1 or column_index == 0 or column_index == max_y_dimension-1:
                continue
            return

             
                # edge_case_count += 1
            # print(f"Edge Case Count: {edge_case_count}")
    
# 5. Within nested for loops, we will need two sections of code: first, detect if we are at an edge case (if statement) and will skip this iteration of the for loops if so. Second, will detect the local minimum value.
# 6. Inside the second bit, that is what we are using to detect if the current central value is minimum to everything else.
# (Will look at above, below, left, right values)
# Central point

def main():
    data = get_data(FILE_PATH)
    access_element(data)

if __name__ == "__main__":
    main()

