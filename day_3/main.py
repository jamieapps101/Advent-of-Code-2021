FILE_PATH = "./day_3/data/input.txt"

def import_diagnostic_report(file_path: str):
    input_data = []
    with open(file_path) as fp:
        for line in fp:
            input_data.append(line[:-1])
    return input_data

def scan_data(input_data):
    gamma_rate = 0
    epsilon_rate = 0


def main():
    input_data = import_diagnostic_report(FILE_PATH)
    print(input_data)


if __name__=="__main__":
    main()
