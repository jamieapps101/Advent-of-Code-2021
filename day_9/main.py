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
    for row_index in range(max_y_dimension):
        column = []
        for column_index in range(max_x_dimension):
            # target = row_index[column_index]
            # column.append(target)
            item = line_data[row_index][column_index]
            return item
    # print(column)


# for each column index
#     for column_index in range(number_of_columns):
#         # visits each string in input_data, and gets the character
#         # at the index of column_index
#         column = []
#         for row in input_data:
#             x = row[column_index]
#             column.append(x)
#         # count number of 1s and 0s in string
#         ones = column.count("1")
#         zeroes = column.count("0")
#         # Build up string representation of binary number for each column
#         gamma_rate   += "1" if ones>zeroes else "0"
#         epsilon_rate += "1" if ones<zeroes else "0"
#     # once we've built up the binary strings, convert them into actual
#     # integer numbers






# 2. Two nested for loops, one iterating from 0 to xmax, second iterating from 0 to ymax.
# 3. Use double slicing syntax to access a particular element in the square (see example)
# 4. Build model that works on standard digits e.g. all 4 dimensions (doing edge cases later)

def main():
    data = get_data(FILE_PATH)
    access_element(data)

if __name__ == "__main__":
    main()

