from typing import List

FILE_PATH = "./day_3/data/input.txt"

def import_diagnostic_report(file_path: str):
    '''Takes a path to the report data, and returns a list of strings where each
    string is a line'''
    input_data = []
    with open(file_path) as fp:
        for line in fp:
            input_data.append(line[:-1])
    return input_data

def binary_string_to_int(input_str):
    '''Takes a string '''
    int_value = 0
    for bit in input_str:
        int_value *= 2
        if bit == "1":
            int_value += 1
    return int_value

def scan_data(input_data):
    gamma_rate   = ""
    epsilon_rate = ""
    number_of_columns = len(input_data[0])
    for column_index in range(number_of_columns):
        column = [row[column_index] for row in input_data]
        ones = column.count("1")
        zeroes = column.count("0")
        gamma_rate   += "1" if ones>zeroes else "0"
        epsilon_rate += "1" if ones<zeroes else "0"
    gamma_rate_value   = binary_string_to_int(gamma_rate)
    epsilon_rate_value = binary_string_to_int(epsilon_rate)

    power_consumption = gamma_rate_value*epsilon_rate_value
    print(f"power_consumption: {power_consumption}")

def build_branch(row: str, local_tree: dict, depth: int):
    # depth is in relation to the character counter
    if depth == len(row):
        # returns the value at the end of the branch
        return row
    else:
        bit = row[depth]
        if bit not in local_tree:
            local_tree[bit] = {}
            local_tree[bit+"_count"] = 0
        else:
            # dont need to add it
            local_tree[bit+"_count"] += 1

        local_tree[bit] = build_branch(row,local_tree[bit],depth+1)
        # return the modified local tree to be reflected by this
        # function's caller
        return local_tree

def build_tree(diagnostic_report_data: List[str]):
    '''Function to build a recursive data structure to represent report
    data values'''
    global_tree = {}
    for row in diagnostic_report_data:
        # row = "010111011001"
        depth = 0
        # build_branch builds a branch into the global_tree by passing the current
        # value of global_tree into the local tree argument of build branch
        # build_branch then modifies the local_tree variable, and returns its
        # new value to be reassigned to the global_tree variable.
        global_tree = build_branch(row,global_tree,depth)
    return global_tree


def query_tree(tree):
    '''For Liv!'''
    pass


def main():
    input_data = import_diagnostic_report(FILE_PATH)
    tree = build_tree(input_data)

if __name__=="__main__":
    main()


#      * 00
#     /
# 0x * \
#   /   * 01
# *
#   \ /* 10
# 1x *
#     \
#      * 11


node["0"]["0"] -> "00"



node["0"] -> {
    "0": "00",
    "0_count": 1,
    "1": "01",
    "1_count": 1,
}

# 00, 01, 10, 11
#
#
#


# node = { "1":[], "0":[] }
# sub_node = { "value": "1010001" }


# node["1"].append(sub_node)


# node["1"]["0"]["1"]["0"][]


a={"x":4,"y":5,"z":9}


