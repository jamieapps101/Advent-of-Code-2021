#! /usr/bin/env python3

from typing import List,Tuple

FILE_PATH = "day_6/data/input.txt"

class LanternfishGroup:
    def __init__(self,internal_timer:int,replicas:int,reset_value:int):
        self.internal_timer = internal_timer
        self.reset_value = reset_value
        self.replicas = replicas

    def lanternfish_age(self):
        if self.internal_timer == 0:
            self.internal_timer = self.reset_value
            return True
        else:
            self.internal_timer -= 1
            return False

class School:
    def __init__(self,existing_fish_age:List[Tuple[int,int]]):
        self.day_counter = 0
        self.lfg_list = [LanternfishGroup(age_replicas[0],age_replicas[1],6) for age_replicas in existing_fish_age]

    def school_age_up(self):
        child_replicas = 0
        for index in range(len(self.lfg_list)):
            has_child = self.lfg_list[index].lanternfish_age()
            if has_child is True:
                child_replicas += self.lfg_list[index].replicas
        return child_replicas

    def baby_lanternfish(self,child_replicas:int):
        if child_replicas > 0:
            self.lfg_list.append(LanternfishGroup(8,child_replicas,6))

    def school_register(self) -> int:
        return sum([group.replicas for group in self.lfg_list])

    def census(self):
        for lfg in self.lfg_list:
            print(f"{lfg.internal_timer}x{lfg.replicas},",end="")
        print("")

    def time_passes(self,days:int):
        day_target = days + self.day_counter
        while self.day_counter < day_target:
            # print(f"day: {self.day_counter}, fish: {self.school_register()}")
            # self.census()
            # print("")
            new_children = self.school_age_up()
            self.baby_lanternfish(new_children)
            self.day_counter += 1

def get_data(file_path: str) -> List[int]:
    input_data = []
    with open(file_path) as fp:
        for line in fp:
            input_data.extend([int(n) for n in line.split(",")])
    return input_data

def group_data(data) -> List[Tuple[int,int]]:
    grouped_data = {}
    for d in data:
        if d not in grouped_data:
            grouped_data[d] = 1
        else:
            grouped_data[d] += 1
    grouped_data = [(k,grouped_data[k]) for k in grouped_data]
    return grouped_data

def main():
    # data = get_data(FILE_PATH)
    data = group_data(get_data(FILE_PATH))
    # data = [(3,2),(4,1),(1,1),(2,1)]
    school = School(data)
    # school.census()
    school.time_passes(256)

    print(f"School Register: {school.school_register()}")

if __name__=="__main__":
    main()