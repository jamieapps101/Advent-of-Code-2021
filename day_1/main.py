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
        if i < 2:
            continue
        elif i == 2:
            deltas.append("N/A")
        else:
            # start on the 4th element, but look back at
            # the first 3
            first_triple  = input_data[i-3:i]
            second_triple = input_data[i-2:i+1]

            first_sum = sum(first_triple)
            second_sum = sum(second_triple)

            if first_sum < second_sum:
                deltas.append("increase")
                increase_counter += 1
            elif first_sum > second_sum:
                deltas.append("decrease")
                decrease_counter += 1
            else:
                deltas.append("equal")
                equal_counter += 1
    

    print("increase_counter: {}".format(increase_counter))
    print("decrease_counter: {}".format(decrease_counter))
    print(f"equal_counter: {equal_counter}")
    return deltas




def main():
    print("Starting")
    input_data = get_input_data(FILE_PATH)
    deltas = get_deltas(input_data)
    print(deltas[0:8])





if __name__=="__main__":
    main()