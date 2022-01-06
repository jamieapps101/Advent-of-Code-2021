#! /usr/bin/env python3

from typing import List

FILE_PATH = "day_8/data/input.txt"

# 1 = 2 segments
# 4 = 4 segments
# 7 = 3 segments
# 8 = 7 segments
# We need to identify how many times these numbers appear in the output.

def get_data(file_path: str):
    input_data = []
    with open(file_path) as fp:
        for line in fp:
            input_data = [l.rstrip() for l in line.split(" | ")]
            # unique_signal_patterns = input_data[0].split()
            four_digit_output_values = input_data[1].split()
            # print(f"Unique Signal Patterns: {unique_signal_patterns}")
            print(f"Output Values: {four_digit_output_values}")
    return four_digit_output_values
    # four_digit_output_values = input_data[1].split()

def segment_counter(four_digit_output_values: List[List[str]]):
    ones = 0
    fours = 0
    sevens = 0
    eights = 0
    for line in four_digit_output_values:
        print(line[0])
        print(line[1])
        print(line[2])
        print(line[3])
        if len(line[0])== 2:
            ones += 1
        elif len(line[0])== 4:
            fours += 1
        elif len(line[0])== 3:
            sevens += 1
        elif len(line[0])== 7:
            eights += 1
        elif len(line[1])== 2:
            ones += 1
        elif len(line[1])== 4:
            fours += 1
        elif len(line[1])== 3:
            sevens += 1
        elif len(line[1])== 7:
            eights += 1
        elif len(line[2])== 2:
            ones += 1
        elif len(line[2])== 4:
            fours += 1
        elif len(line[2])== 3:
            sevens += 1
        elif len(line[2])== 7:
            eights += 1
        elif len(line[3])== 2:
            ones += 1
        elif len(line[3])== 4:
            fours += 1
        elif len(line[3])== 3:
            sevens += 1
        elif len(line[3])== 7:
            eights += 1
        else:
            pass
    print(f"Number of ones: {ones}")
    print(f"Number of fours: {fours}")
    print(f"Number of sevens: {sevens}")
    print(f"Number of eights: {eights}")
    total_number = ones + fours + sevens + eights
    print(f"Total Number: {total_number}")

def main():
    data = get_data(FILE_PATH)
    segment_counter(data)

if __name__=="__main__":
    main()

