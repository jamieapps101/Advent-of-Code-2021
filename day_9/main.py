#! /usr/bin/env python3

FILE_PATH = "day_9/data/input.txt"

def get_data(file_path: str):
    line_data = []
    with open(file_path) as fp:
        for line in fp:
            line = line.rstrip()
            digit_data = []
            for digit in line:
                number = int(digit)
                digit_data.append(number)
            line_data.append(digit_data)
    # print(f"Digit Data = {digit_data}")
    # print(f"Line Data = {line_data}")
    print(f"Input Data = {line_data}")
    return line_data

def main():
    data = get_data(FILE_PATH)

if __name__ == "__main__":
    main()


# so I would go through each line, convert it to a list of ints. then append that list into the input_data list
