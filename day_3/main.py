FILE_PATH = "./day_3/data/input.txt"

def import_diagnostic_report(file_path: str):
    input_data = []
    with open(file_path) as fp:
        for line in fp:
            input_data.append(line[:-1])
    return input_data


def binary_string_to_int(input_str):
    int_value = 0
    for bit in input_str:
        int_value *= 2
        if bit == "1":
            int_value += 1
    return int_value



def scan_data(input_data):
    gamma_rate   = ""
    epsilon_rate = ""

    number_of_columns = len(input_data[0])

    for column_index in range(number_of_columns):
        column = [row[column_index] for row in input_data]
        ones = column.count("1") 
        zeroes = column.count("0") 

        gamma_rate += "1" if ones>zeroes else "0"
        epsilon_rate += "1" if ones<zeroes else "0"

    gamma_rate_value = binary_string_to_int(gamma_rate)
    epsilon_rate_value = binary_string_to_int(epsilon_rate)


    power_consumption = gamma_rate_value*epsilon_rate_value
    print(f"power_consumption: {power_consumption}")




def main():
    input_data = import_diagnostic_report(FILE_PATH)
    # print(input_data)
    scan_data(input_data)

    # print(binary_string_to_int("0101"))


if __name__=="__main__":
    main()
