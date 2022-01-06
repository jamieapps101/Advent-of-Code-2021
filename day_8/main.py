#! /usr/bin/env python3

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
            unique_signal_patterns = input_data[0].split()
            four_digit_output_values = input_data[1].split()
            print(f"Unique Signal Patterns: {unique_signal_patterns}")
            print(f"Output Values: {four_digit_output_values}")

def main():
    data = get_data(FILE_PATH)

if __name__=="__main__":
    main()