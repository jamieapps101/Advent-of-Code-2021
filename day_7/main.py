#! /usr/bin/env python3

from typing import List

FILE_PATH = "day_7/data/input.txt"

def get_data(file_path: str):
    input_data = []
    with open(file_path) as fp:
        for line in fp:
            input_data.extend([int(n) for n in line.split(",")])
    # print(f"Crab Submarine Positions: {input_data}")
    # print(f"Number of Crab Submarines: {len(input_data)}")
    return input_data

def max_current_position(positions: List[int]):
    return max(positions)

def min_current_position(positions: List[int]):
    return min(positions)

def fuel_cost(current_positions: List[int], proposed_position: int):
    absolute_difference = 0
    for position in current_positions:
        if position >= proposed_position:
            absolute_difference += position - proposed_position
        else:
            absolute_difference += proposed_position - position
    print(f"Absolute Difference: {absolute_difference}")
    return absolute_difference
    # get absolute difference between 'proposed' position and actual position of each item in the list
    # sum absolute differences up

def main():
    data = get_data(FILE_PATH)
    fuel_cost(data,750)
    maximum_current_position = max_current_position(data)
    print(f"Maximum Current Position: {maximum_current_position}")
    minimum_current_position = min_current_position(data)
    print(f"Minimum Current Position: {minimum_current_position}")

if __name__=="__main__":
    main()