#! /usr/bin/env python3

from typing import List

FILE_PATH = "day_6/data/input.txt"

class Lanternfish:
    def __init__(self,internal_timer:int,reset_value:int):
        self.internal_timer = internal_timer
        self.reset_value = reset_value

    def lanternfish_age(self):
        if self.internal_timer == 0:
            self.internal_timer = self.reset_value
            return True
        else:
            self.internal_timer -= 1
            return False

class School:
    def __init__(self,existing_fish_age:List[int]):
        self.day_counter = 0
        self.lanternfish_list = [Lanternfish(age,6) for age in existing_fish_age]

    def school_age_up(self):
        child_counter = 0
        for index in range(len(self.lanternfish_list)):
            has_child = self.lanternfish_list[index].lanternfish_age()
            if has_child is True:
                child_counter += 1
        return child_counter

    def baby_lanternfish(self,child_counter:int):
        for new_babies in range(child_counter):
            self.lanternfish_list.append(Lanternfish(0,8))

    def school_register(self) -> int:
        return len(self.lanternfish_list)

    def time_passes(self,days:int):
        day_target = days + self.day_counter
        while self.day_counter < day_target:
            print(f"day: {self.day_counter}")
            new_children = self.school_age_up()
            self.baby_lanternfish(new_children)
            self.day_counter += 1

def get_data(file_path: str):
    input_data = []
    with open(file_path) as fp:
        for line in fp:
            input_data.extend([int(n) for n in line.split(",")])
    return input_data

def main():
    data = get_data(FILE_PATH)
    lanternfish_school = School(data)
    lanternfish_school.time_passes(80)

    print(f"School Register: {lanternfish_school.school_register()}")

if __name__=="__main__":
    main()