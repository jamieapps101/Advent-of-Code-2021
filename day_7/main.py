#! /usr/bin/env python3

from typing import List,Tuple

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
    return absolute_difference
    # get absolute difference between 'proposed' position and actual position of each item in the list
    # sum absolute differences up

def mean(a,b):
    return (a+b)/2

def get_solution(data: List[int], precision: int = 10) -> Tuple[int,int]:
    a = max(data)
    c = min(data)
    b = mean(a,c)
    for i in range(precision):
        print(f"{i}) a={a}, c={c} - ",end="")
        candidate_a = mean(a,b)
        candidate_a_cost = fuel_cost(data,candidate_a)
        candidate_b = mean(b,c)
        candidate_b_cost = fuel_cost(data,candidate_b)
        if candidate_a_cost <= candidate_b_cost:
            a = a
            c = b
        else:
            a = b
            c = c
        b = mean(a,c)
        print(f"cost={fuel_cost(data,b)}")
    return (b,fuel_cost(data,b))

def main():
    data = get_data(FILE_PATH)
    fuel_cost(data,750)
    maximum_current_position = max_current_position(data)
    print(f"Maximum Current Position: {maximum_current_position}")
    minimum_current_position = min_current_position(data)
    print(f"Minimum Current Position: {minimum_current_position}")
    solution = get_solution(data,precision=20)

    print(f"solution is {int(solution[0])} with cost {int(solution[1])}")

if __name__=="__main__":
    main()