from typing import List


FILE_PATH = "./day_2/data/input.txt"


def import_instructions(file_path: str):
    instructions = []
    # fp = open(file_path)
    with open(file_path) as fp:
        for line in fp:
            # This reads in each line in the file
            # and puts it onto the end of the
            # instructions list
            # instructions.append(line)
            if line == "":
                break
            parts = line.split()
            keyword = parts[0]
            value = int(parts[1])
            instructions.append({
                "keyword": keyword,
                "value": value
            })
    return instructions


def act_on_instructions(instructions: List[dict]):
    horizontal_position = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        if instruction["keyword"] == "forward":
            horizontal_position += instruction["value"]
            depth += aim * instruction["value"]
        elif instruction["keyword"] == "up":
            aim -= instruction["value"]
        elif instruction["keyword"] == "down":
            aim += instruction["value"]
        else:
            print("ERRRRRRRRRRRor")
            raise Exception
    final_position = horizontal_position * depth
    print(f"final_position: {final_position}")


def main():
    instructions = import_instructions(FILE_PATH)
    act_on_instructions(instructions)



if __name__ == "__main__":
    main()
