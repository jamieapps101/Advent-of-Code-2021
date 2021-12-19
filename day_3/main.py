from typing import List
from enum import Enum

FILE_PATH = "./day_3/data/input.txt"

def import_diagnostic_report(file_path: str):
    '''Takes a path to the report data, and returns a list of strings where each
    string is a line'''
    input_data = []
    with open(file_path) as fp:
        for line in fp:
            input_data.append(line[:-1])
    return input_data

def binary_string_to_int(input_str: str):
    '''Takes a string '''
    int_value = 0
    for bit in input_str:
        int_value *= 2 # -> int_value = int_value*2
        if bit == "1":
            int_value += 1
    return int_value

# input_str = "0110"
#
# iteration counter | bit | int_value
# -1                | X   | 0
#  0                | "0" | 0
#  1                | "1" | 1
#  2                | "1" | 3
#  3                | "0" | 6

def scan_data(input_data: List[str]):
    gamma_rate   = ""
    epsilon_rate = ""
    number_of_columns = len(input_data[0])

    # 12 -> [0 1 2 3 4 5 6 7 8 9 10 11]
    # column_index = 0
    # column_index = 1
    # column_index = 2
    # column_index = 3
    # column_index = 4
    # column_index = 5
    # column_index = 6
    # column_index = 7
    # ...

    # for each column index
    for column_index in range(number_of_columns):
        # visits each string in input_data, and gets the character
        # at the index of column_index
        column = []
        for row in input_data:
            x = row[column_index]
            column.append(x)
        # count number of 1s and 0s in string
        ones = column.count("1")
        zeroes = column.count("0")
        # Build up string representation of binary number for each column
        gamma_rate   += "1" if ones>zeroes else "0"
        epsilon_rate += "1" if ones<zeroes else "0"
    # once we've built up the binary strings, convert them into actual
    # integer numbers
    gamma_rate_value   = binary_string_to_int(gamma_rate)
    epsilon_rate_value = binary_string_to_int(epsilon_rate)

    # Follow the guidance for finding the power consumption
    power_consumption = gamma_rate_value*epsilon_rate_value
    print(f"power_consumption: {power_consumption}")

def build_branch(row: str, local_tree: dict, depth: int):
    if depth == len(row):
        return row
    else:
        bit = row[depth]
        if bit not in local_tree:
            local_tree[bit] = {}
            local_tree[bit+"_count"] = 0
        else:
            local_tree[bit+"_count"] += 1

        local_tree[bit] = build_branch(row,local_tree[bit],depth+1)
        return local_tree

def build_tree(diagnostic_report_data: List[str]):
    '''Function to build a recursive data structure to represent report
    data values'''
    global_tree = {}
    for row in diagnostic_report_data:
        # row = "010111011001"
        depth = 0
        global_tree = build_branch(row,global_tree,depth)
    return global_tree

class TreeQueryMode(Enum):
    LEAST_COMMON=0
    MOST_COMMON =1

def query_tree(tree, mode: TreeQueryMode):
    if mode == TreeQueryMode.MOST_COMMON:
        filter_bit = "1" if tree["1_count"] > tree["0_count"] else "0"



def main():
    input_data = import_diagnostic_report(FILE_PATH)
    tree = build_tree(input_data)

if __name__=="__main__":
    main()


