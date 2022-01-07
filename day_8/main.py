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
    # print(f"FDOV: {four_digit_output_values}")
    return unique_signal_patterns,four_digit_output_values

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


def in_common_with(a,b):
    a = sorted(a)
    b = sorted(b)
    return sum([x in a for x in b])


def create_lookup_table(line: List[str]):
    digits = [sorted(d) for d in line]

    lut = [None for i in range(10)]

    # decode the obvious ones
    for d in digits:
        if   len(d)== 2:
            lut[1] = d
        elif len(d)== 4:
            lut[4] = d
        elif len(d)== 3:
            lut[7] = d
        elif len(d)== 7:
            lut[8] = d

    # now the harder ones
    for d in digits:
        if len(d) == 6:
            # this could be a 0,6,9
            if in_common_with(d,lut[1])==1:
                # 6 has 1 in common with 1
                lut[6] = d
            elif in_common_with(d,lut[4])==4:
                # 9 has 4 in commonn with 4
                lut[9] = d
            else:
                # 0 otherwise
                lut[0] = d

        elif len(d) == 5:
            # this could be a 2,3,5
            if in_common_with(d,lut[1])==2:
                # 3 has 2 in common with a 1
                lut[3] = d
            elif in_common_with(d,lut[4])==2:
                # 2 has 2 in common with 4
                lut[2] = d
            else:
                # 5 has 5 in common with 6
                lut[5] = d
    # build a reverse lut
    # for i in range(len(lut)):
    #     print(f"{i}) {lut[i]}")
    return {"".join(lut[i]):i for i in range(len(lut)) if lut[i] is not None}

def decoder(lut,fdov):
    # sort the fodvs
    fdov = ["".join(sorted(v)) for v in fdov]
    value = 0
    for o in fdov:
        value *= 10
        value += lut[o]
    return value

def test_create_lookup_table():
    sample = ["acedgfb","cdfbe","gcdfa","fbcad","dab","cefabd","cdfgeb","eafb","cagedb","ab"]
    lut = create_lookup_table(sample)
    print(f"lut: {lut}")

def main():
    usp,fdov = get_data(FILE_PATH)
    values = []
    for index in range(len(usp)):
        lut = create_lookup_table(usp[index])
        values.append(decoder(lut,fdov[index]))
    summed_value = sum(values)
    print(f"summed_value: {summed_value}")

if __name__=="__main__":
    main()
