#! /usr/bin/env python3

from typing import List

FILE_PATH = "day_9/data/test_input.txt"
# FILE_PATH = "day_9/data/input.txt"

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
    return line_data

def basin_labeller(line_data: List):
    pass
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



'''
0. read in data into matrix format
1. create extra dimension to allow labelling
2. pass over each element
    2a. if adjacent elements are in basins, copy over basin id
    2b. if no adjacent elements are in basins, use basin counter value
    as new id, and increment basin counter
'''


def create_label_dim(depth_data: List[List[int]]) -> List[List[dict]]:
    '''Replace each integer depth measurement with a dictionary containing
    the depth, and an optional label value'''
    for y in range(len(depth_data)):
        for x in range(len(depth_data[0])):
            depth = depth_data[y][x]
            depth_data[y][x] = {
                "depth": depth,
                "label": None
            }
    return depth_data

def basin_finder(depth_data: List[List[int]]) -> List[List[dict]]:
    depth_data = create_label_dim(depth_data)
    basin_counter = 0
    basin_size_count = []

    for y in range(len(depth_data)):
        for x in range(len(depth_data[0])):
            print(f"depth: {depth_data[y][x]['depth']} | ",end="")
            if depth_data[y][x]["depth"] < 9:
                # ie we're in a basin
                # determine if there is an adjacent label, and store
                # it in adjacent_label if present
                above = None if y==0 else depth_data[y-1][x]["label"]
                below = None if y==len(depth_data)-1 else depth_data[y+1][x]["label"]
                left  = None if x==0 else depth_data[y][x-1]["label"]
                right = None if x==len(depth_data[0])-1 else depth_data[y][x+1]["label"]
                adjacent_labels = [above, below, left, right]
                adjacent_label = None
                for l in adjacent_labels:
                    if l is not None:
                        adjacent_label = l
                        break
                print(f"adjacent_label: {adjacent_label} | adjacent_labels: {adjacent_labels}")

                if adjacent_label is None:
                    # ie there are no other basin measurements nearby,
                    # so we must be in a new basin
                    depth_data[y][x]["label"] = basin_counter
                    basin_size_count.append(1)
                    basin_counter += 1
                else:
                    # there is an adject basin nearby! we'll copy the label that we identified
                    depth_data[y][x]["label"] = adjacent_label
                    basin_size_count[adjacent_label] += 1
            else:
                # ie we're not in a basin, so do nothing
                print("")
                pass
        print("<new row>")

    return depth_data,basin_size_count

def main():
    data = get_data(FILE_PATH)

    _depth_data,basin_size_count = basin_finder(data)

    sorted(basin_size_count,reverse=True)

    top_three_basin_sizes = basin_size_count[0:3]
    multiplied_sizes = 1
    for size in top_three_basin_sizes:
        multiplied_sizes *= size

    # 98532 - too low
    print(f"multiplied_sizes: {multiplied_sizes}")



if __name__ == "__main__":
    main()

