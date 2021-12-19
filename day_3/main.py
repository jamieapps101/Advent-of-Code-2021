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

def build_tree(diagnostic_report_data: List[str]):
    '''Function to build a recursive data structure to represent report
    data values'''
    global_tree = {}
    for row in diagnostic_report_data:
        # row = "010111011001"
        depth = 0
        global_tree = build_branch(row,global_tree,depth)
    return global_tree

def build_branch(row: str, local_tree: dict, depth: int):
    if depth == len(row):
        return row
    else:
        # we use depth to find the character in the "row" string, that
        # we are interested in.
        bit = row[depth]
        if bit not in local_tree:
            local_tree[bit] = {}
            local_tree[bit+"_count"] = 1
        else:
            # local_tree[bit] = ?
            local_tree[bit+"_count"] += 1

        local_tree[bit] = build_branch(row,local_tree[bit],depth+1)
        return local_tree

'''
    ######## EXAMPLE #######
    diagnostic_report_data = ["010","000","011"]
    global_tree = {}
    row = "010"
    depth = 0
    >>build_branch>>
        (row = "010")
        (local_tree = {})
        (depth = 0)
        bit = "0"
        local_tree = {"0":{}}
        local_tree = {"0":{},"0_count":1}
        >>build_branch>>
            (row = "010")
            (local_tree = {})
            (depth = 1)
            bit = "1"
            local_tree = {"1":{}}
            local_tree = {"1":{},"1_count":1}
            >>build_branch>>
                (row="010")
                (local_tree={})
                (depth=2)
                bit="0"
                local_tree = {"0":{}}
                local_tree = {"0":{},"0_count":1}
                >>build_branch>>
                    (row="010")
                    (local_tree={})
                    (depth=3)
                    <return "010">
                local_tree = {
                    "0":"010",
                    "0_count":1
                }
            local_tree = {
                "0":{
                    "0":"010",
                    "0_count":1
                },
                "0_count":1
            }
        local_tree = {
            "0": {
                "1":{
                    "0":"010",
                    "0_count":1
                },
                "1_count":1
            }
            "0_count": 1
        }
    global_tree = {
            "0": {
                "1":{
                    "0":"010",
                    "0_count":1
                },
                "1_count":1
            }
            "0_count": 1
        }
    row = "000"
    >>build_branch>>
        (row = "000")
        (local_tree = {"0": {"1":{"0":"010","0_count":1},"1_count":1},"0_count": 1})
        (depth = 0)
        bit = "0"
        local_tree = {"0": {"1":{"0":"010","0_count":1},"1_count":1},"0_count": 2}
        >>build_branch>>
            (row = "000")
            (local_tree = {"1":{"0":"010","0_count":1},"1_count":1})
            (depth = 1)
            bit = "0"
            local_tree = {"1":{"0":"010","0_count":1},"1_count":1,"0":{},"0_count":1}
            >>build_branch>>
                (row = "000")
                (local_tree = {})
                (depth=2)
                bit="0"
                local_tree = {"0":{}}
                local_tree = {"0":{},"0_count":1}
                >>build_branch>>
                    (row = "000")
                    (local_tree = {})
                    (depth=3)
                    <return "000">
                local_tree = {
                    "0":"000",
                    "0_count":1
                }
            local_tree = {
                "1":{
                    "0":"010",
                    "0_count":1
                },
                "1_count":1,
                "0":{
                    "0":"000",
                    "0_count":1
                },
                "0_count":1
            }
        local_tree = {
            "0": {
                "1":{
                    "0":"010",
                    "0_count":1
                },
                "1_count":1,
                "0":{
                    "0":"000",
                    "0_count":1
                },
                "0_count":1
            },
            "0_count":2
        }
    global_tree = {
            "0": {
                "1":{
                    "0":"010",
                    "0_count":1
                },
                "1_count":1,
                "0":{
                    "0":"000",
                    "0_count":1
                },
                "0_count":1
            },
            "0_count":2
        }

    ...

    global_tree = {
            "0": {
                "1":{
                    "0":"010",
                    "0_count":1,
                    "1":"011",
                    "1_count":1
                },
                "1_count":2,
                "0":{
                    "0":"000",
                    "0_count":1
                },
                "0_count":1
            },
            "0_count":3
        }

    ########################
'''

class TreeQueryMode(Enum):
    OXY_MODE = 0
    CO_MODE = 1

def pretty_print(string: str, indent: int):
    print("  "*indent+string)

def query_tree(tree, mode: TreeQueryMode,depth=0):
    if isinstance(tree,dict):
        if "0_count" not in tree:
            return query_tree(tree["1"],mode,depth+1)
        elif "1_count" not in tree:
            return query_tree(tree["0"],mode,depth+1)
        else:
            if mode == TreeQueryMode.OXY_MODE:
                filter_bit = "1" if tree["1_count"]>=tree["0_count"] else "0"
            elif mode == TreeQueryMode.CO_MODE:
                filter_bit = "0" if tree["0_count"]<=tree["1_count"] else "1"
            return query_tree(tree[filter_bit],mode,depth+1)
    else:
        return tree

def get_oxy_gen_rating(tree):
    '''Filter by most common value'''
    return query_tree(tree, TreeQueryMode.OXY_MODE)

def get_co2_scr_rating(tree):
    '''Filter by most common value'''
    return query_tree(tree, TreeQueryMode.CO_MODE)

def main():
    input_data = import_diagnostic_report(FILE_PATH)
    tree = build_tree(input_data)

    og_rating_str = get_oxy_gen_rating(tree)
    print(f"og_rating_str: {og_rating_str}")
    og_rating = binary_string_to_int(og_rating_str)

    cs_rating_str = get_co2_scr_rating(tree)
    print(f"cs_rating_str: {cs_rating_str}")
    cs_rating = binary_string_to_int(cs_rating_str)

    life_support_rating = og_rating * cs_rating
    print(f"life_support_rating: {life_support_rating}")
    # 3853616 too high


if __name__=="__main__":
    main()


