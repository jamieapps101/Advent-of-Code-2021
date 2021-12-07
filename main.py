#! /usr/bin/env python3


FILE_PATH = "./data/input.txt"


def get_input_data(path: str):
    input_data = []
    with open(FILE_PATH) as fp:
        for line in fp:
            number = int(line)
            input_data.append(number)
    return input_data


def get_deltas(input_data):
    deltas = []
    increase_counter = 0
    decrease_counter = 0
    equal_counter = 0
    for i in range(len(input_data)):
        if i == 0:
            deltas.append("N/A")
            continue
        else:
            if input_data[i-1] < input_data[i]:
                deltas.append("increase")
                increase_counter += 1
            elif input_data[i-1] > input_data[i]:
                deltas.append("decrease")
                decrease_counter += 1
            else:
                deltas.append("equal")
                equal_counter += 1
    
    print("increase_counter: {}".format(increase_counter))
    print("decrease_counter: {}".format(decrease_counter))
    print(f"equal_counter: {equal_counter}")




def main():
    print("Starting")
    input_data = get_input_data(FILE_PATH)
    get_deltas(input_data)




if __name__=="__main__":
    main()