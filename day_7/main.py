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

def fuel_calculator(trip_distance:int):
    cumulative_fuel_cost = 0
    for x in range(trip_distance):
        cumulative_fuel_cost = 1 + x + cumulative_fuel_cost
        # print(f"Fuel Calculator: {x}")
        # print(f"CFC: {cumulative_fuel_cost}")
    return cumulative_fuel_cost
        
def fuel_cost(current_positions: List[int], proposed_position: int):
    trip_cost = 0
    for position in current_positions:
        if position >= proposed_position:
            trip_cost += fuel_calculator(position - proposed_position)
        else:
            trip_cost += fuel_calculator(proposed_position - position)
    print(f"Absolute Difference: {trip_cost}")
    return trip_cost
    # get absolute difference between 'proposed' position and actual position of each item in the list
    # sum absolute differences up

def get_solution(data: List[int],min_current_position: int, max_current_position: int):
    lowest_cost = 0
    best_position = 0
    for position in range(min_current_position,max_current_position + 1):
        position_cost = fuel_cost(data,position)
        if position == min_current_position:
            lowest_cost = position_cost
            best_position = position
            print(f"Lowest Cost: {lowest_cost}")
            print (f"Best Position: {best_position}")
        elif position_cost < lowest_cost:
            lowest_cost = position_cost
            best_position = position
    return lowest_cost,best_position
# max/min positions
# iterate over values in that range for possible solutions
# for each possible solution, call fuel_cost
# identify the lowest number and return it

def main():
    data = get_data(FILE_PATH)
    maximum_current_position = max_current_position(data)
    print(f"Maximum Current Position: {maximum_current_position}")
    minimum_current_position = min_current_position(data)
    print(f"Minimum Current Position: {minimum_current_position}")
    potential_solution = get_solution(data,minimum_current_position,maximum_current_position)
    print(f"Allegedly Lowest Cost: {potential_solution[0]}")
    print(f"Allegedly Best Solution: {potential_solution[1]}")

if __name__=="__main__":
    main()