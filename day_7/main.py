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

def get_triangle_number(n:int) -> int:
    return sum([x+1 for x in range(int(n))])

def fuel_cost(current_positions: List[int], proposed_position: int):
    # get absolute difference between 'proposed' position and actual position of each item in the list
    # sum absolute differences up
    cost = 0
    for position in current_positions:
        cost += get_triangle_number(abs(position - proposed_position))
    return cost

def mean(a,b):
    return (a+b)/2

def get_solution(data: List[int], precision: int = 10) -> Tuple[int,int]:
    a = max(data)
    c = min(data)
    b = mean(a,c)
    for i in range(precision):
        print(f"{i}) a={a}, c={c} - ",end="")
        if fuel_cost(data,int(mean(a,b))) <= fuel_cost(data,int(mean(b,c))):
            # a = a
            c = b
        else:
            a = b
            # c = c
        b = mean(a,c)
        print(f"cost={fuel_cost(data,int(b))}")
    return (b,fuel_cost(data,int(b)))

def main():
    data = get_data(FILE_PATH)
    solution = get_solution(data,precision=15)
    print(f"solution is {int(solution[0])} with cost {int(solution[1])}")

if __name__=="__main__":
    main()