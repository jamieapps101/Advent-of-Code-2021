#! /usr/bin/env python3

FILE_PATH = "./day_5/data/input.txt"

def read_data(file_path: str):
    input_data = []
    with open(file_path) as fp:
        for line in fp:
            arrow_split = line.split(" -> ")
            comma_split = [n.split(",") for n in arrow_split]
            first_x_coordinate = int(comma_split[0][0])
            first_y_coordinate = int(comma_split[0][1])
            second_x_coordinate = int(comma_split[1][0])
            second_y_coordinate = int(comma_split[1][1])
            print(f"first X coordinate: {first_x_coordinate}")
            print(f"second X coordinate: {second_x_coordinate}")
            print(f"first Y coordinate: {first_y_coordinate}")
            print(f"second Y coordinate: {second_y_coordinate}")
    return input_data
        
def main():
    read_data(FILE_PATH)

if __name__=="__main__":
    main()