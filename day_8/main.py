#! /usr/bin/env python3

from typing import List

FILE_PATH = "day_8/data/input.txt"

# 1 = 2 segments
# 4 = 4 segments
# 7 = 3 segments
# 8 = 7 segments
# We need to identify how many times these numbers appear in the output.

def get_data(file_path: str):
    unique_signal_patterns = []
    four_digit_output_values = []
    with open(file_path) as fp:
        for line in fp:
            # use rstrip to remove white space on right side of string
            # which removes the \n character
            split_line = [l.rstrip() for l in line.split(" | ")]
            unique_signal_patterns.append(split_line[0].split())
            four_digit_output_values.append(split_line[1].split())
    print(f"FDOV: {four_digit_output_values}")
    return four_digit_output_values

def segment_counter(four_digit_output_values: List[List[str]]):
    ones = 0
    fours = 0
    sevens = 0
    eights = 0
    for line in four_digit_output_values:
        for word in line:
            if   len(word)== 2:
                ones += 1
            elif len(word)== 4:
                fours += 1
            elif len(word)== 3:
                sevens += 1
            elif len(word)== 7:
                eights += 1

    print(f"Number of ones: {ones}")
    print(f"Number of fours: {fours}")
    print(f"Number of sevens: {sevens}")
    print(f"Number of eights: {eights}")
    total_number = ones + fours + sevens + eights
    print(f"Total Number: {total_number}")

def main():
    data = get_data(FILE_PATH)
    print(f"Data: {data}")
    segment_counter(data)

if __name__=="__main__":
    main()

